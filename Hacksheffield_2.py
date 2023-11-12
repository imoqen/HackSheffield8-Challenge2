import mathsLib
import random
import pandas as pd
import matplotlib.pyplot as plt

class UserData:
    def __init__(self, userID = -1):
        self.userID = userID
        self.setPeriod = []
        self.dateUTC = []
        self.power = []
        self.temp = []

        self.powerChange = []
        self.powerChange2 = []

        self.tempChange = []
        self.tempChange2 = []
    
    def loadData(self,dateUTC, setPeriod, power, temp):
        self.setPeriod.append(float(setPeriod))
        self.dateUTC.append(dateUTC)
        self.power.append(float(power))
        try:
            self.temp.append(float(temp))
        except:
            self.temp.append(0)


def tempEstimation(user):
    forcasts1 = []
    forcasts2 = []
    actuals = []
    for set in range (0,300,1):

        steps = 9
        start = 10 + set
        timesteps = []
        for index in range (1,steps,1):
            timesteps += [index]

        user.tempChange = mathsLib.arrayDiff(user.temp[start:start+steps])
        user.tempChange2 = mathsLib.arrayDiff(user.tempChange)
        mean = mathsLib.arrAverage(user.temp[start:start+steps])
        stdDev = mathsLib.arrStdDev(user.temp[start:start+steps])
    # a,b,rval = mathsLib.liniarRegLineCalc(timesteps,user.tempChange) 13.2% over 300
        a,b,rval = mathsLib.liniarRegLineCalc(timesteps,user.temp[start +1:start+steps])##12.53 over 300
        
        actuals += [user.temp[start + steps + 1]]

        forcasts1 += [((mean+(1-rval)*stdDev) + (mean-((rval)*stdDev)))/2]
        
        ##forcasts2 += [user.temp[len(user.temp)-1] + (user.tempChange[len(user.tempChange)-1] )] ##real bad

    close1 = mathsLib.MAPE(forcasts1,actuals)

    print(user.temp[start:start+steps])
    print(user.tempChange)
    print(user.tempChange2)
    print(close1)


def estimatePowerTrial(user):##put code here
    
    tempweight = 5.65
    mapes  = []
    start = 0
    steps = 0
    for start in range(0,100,1):
        outputArray = []
        for i in range(96):
            outputArray.append([])

        x = 0
        while x < len(user.power) and len(outputArray[95]) < 21:
            outputArray[x%96].append(user.power[start + x])
            x += 1

        averages = []

        for arr in outputArray:
            averages += [mathsLib.arrAverage(arr)]

        stdevs = []

        for arr in outputArray:
            stdevs += [mathsLib.arrStdDev(arr)]

        totalSteps = 0
        for arr in outputArray:
            totalSteps += len(arr)
        steps = totalSteps

        timesteps = []
        for index in range (1,steps,1):
            timesteps += [index]

        usedData = []
        for i in range(0,len(outputArray),1):
            for j in range(0,len(outputArray[i]),1):
                usedData += [outputArray[i][j]]



        a,b,rval = mathsLib.liniarRegLineCalc(timesteps,usedData)

        todaysAverageTemp = mathsLib.arrAverage(user.temp[start:start + len(usedData)])
        tomorrowsAverageTemp = mathsLib.arrAverage(user.temp[start + len(usedData):start + len(usedData)*2])
        tempGrad = mathsLib.gradTwo([1,todaysAverageTemp],[2,tomorrowsAverageTemp])


        adjustedData = []
        for index in range(0,len(averages),1):
            adjustedData += [averages[index] + (averages[index] * rval * tempGrad *tempweight)]

        actualData = user.power[start + len(usedData):start + len(usedData) + 96]

        close1 = mathsLib.MAPE(adjustedData,actualData)
        mapes = [close1]

    averageMape = mathsLib.arrAverage(mapes)
    print(tempweight,averageMape)

def estimatePower(user, start):##put code here
    
    tempweight = 5.65
    mapes  = []
    steps = 0
    
    outputArray = []
    for i in range(96):
        outputArray.append([])

    x = 0
    while x < len(user.power) and len(outputArray[95]) < 21:
        outputArray[x%96].append(user.power[start + x])
        x += 1

    averages = []

    for arr in outputArray:
        averages += [mathsLib.arrAverage(arr)]

    stdevs = []

    for arr in outputArray:
        stdevs += [mathsLib.arrStdDev(arr)]

    totalSteps = 0
    for arr in outputArray:
        totalSteps += len(arr)
    steps = totalSteps

    timesteps = []
    for index in range (1,steps,1):
        timesteps += [index]

    usedData = []
    for i in range(0,len(outputArray),1):
        for j in range(0,len(outputArray[i]),1):
            usedData += [outputArray[i][j]]



    a,b,rval = mathsLib.liniarRegLineCalc(timesteps,usedData)

    todaysAverageTemp = mathsLib.arrAverage(user.temp[start:start + len(usedData)])
    tomorrowsAverageTemp = mathsLib.arrAverage(user.temp[start + len(usedData):start + len(usedData)*2])
    tempGrad = mathsLib.gradTwo([1,todaysAverageTemp],[2,tomorrowsAverageTemp])


    adjustedData = []
    for index in range(0,len(averages),1):
        adjustedData += [averages[index] + (averages[index] * rval * tempGrad *tempweight)]

    actualData = user.power[start + len(usedData):start + len(usedData) + 96]

    close1 = mathsLib.MAPE(adjustedData,actualData)
    mapes = [close1]

    averageMape = mathsLib.arrAverage(mapes)
    
    if (user.userID == "793"):
        output = "Raw power input: "
        for data in usedData:
            output += str(data) + ", "
        print (output)

        output = "Power forecast: "
        for data in adjustedData:
            output += str(data) + ", "
        print (output)

        output = "Actual power: "
        for data in actualData:
            output += str(data) + ", "
        print(output)
    
    return tempweight,averageMape

##file reading and data assigning

dataFile = open("fullDataSet.csv","r")

data = dataFile.read()

dataList = data.split("\n")

userDictionary = {}
listOfUsers = []

firstLine = False

for dataLine in dataList:
    if not firstLine:
        firstLine = True
        continue
    
    dataLineList = dataLine.split(",")
    
    if len(dataLineList) < 6:
        continue

    if dataLineList[0] not in userDictionary:
        newItem = UserData(dataLineList[0])
        newItem.loadData(dataLineList[1],dataLineList[3],dataLineList[4],dataLineList[5])
        userDictionary[dataLineList[0]] = newItem
        listOfUsers.append(dataLineList[0])
    
    else:
        userDictionary[dataLineList[0]].loadData(dataLineList[1],dataLineList[3],dataLineList[4],dataLineList[5])

print("Data Processed!")

IDs = []
for userID in userDictionary:
    IDs.append(userID)
    


def runOnRandomNumOfUsers(num):
    for i in range(num):
        value = random.choice(IDs)
        weight,avMape = estimatePower(userDictionary[value], 0)
        print("User",value,":",avMape)
        
def runOnSpecificUser(userID):
    weight,avMape = estimatePower(userDictionary[userID], 0)
    print("User",userID," MAPE :",avMape)
        
        
def runOnAllUsers():
    allValues = []
    errorCount = 0
    for value in IDs:
        try:
            weight,avMape = estimatePower(userDictionary[value], 0)
        except:
            print("User",value,"Had erroneous data")
            errorCount += 1
        else:
            print("User",value,":",avMape)
            allValues.append(avMape)
    print("Mean :",mathsLib.arrAverage(allValues))
    print("Erreoneous Users :",errorCount)

##close2 = mathsLib.MAPE(forcasts2,actuals)

runOnAllUsers()

print("\nCase study, User 793:")

runOnSpecificUser("793")

