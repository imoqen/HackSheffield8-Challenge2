import math
def arrAverage(numbers): ## average of arrays
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return (average)

def arrStdDev(numbers):

    mean = arrAverage(numbers)
    total = 0
    for num in numbers:
        total += (num - mean)**2
    stdDev = math.sqrt(total/len(numbers))
    return (stdDev)

def MAPE(forcast, actual):## forcast data values in array, actual values in an array
    n = len(forcast)
    invs = 1/n
    sumof = 0
    for index in range (0, len(forcast), 1):
        
        sumof += abs(actual[index]-forcast[index]) / actual[index]
    acc = round(invs * sumof *100 , 2)
    return (acc)

def gradTwo(coord1, coord2):
    grad = (coord1[1] - coord2[1])/(coord1[0]-coord2[0])
    return (grad)


def liniarRegLineCalc(x, y):## x and y are arrays 
    sum_y = 0
    sum_y2 = 0
    sum_x = 0
    sum_x2 = 0
    sum_xy = 0
    n = len(x)
    a = 0
    b = 0 
    for indy in y:##total y and y**2
        sum_y += indy
        sum_y2 += indy**2

    for indx in x:##total x and x**2
        sum_x += indx
        sum_x2 += indx**2
        
    for index in range (0,len(x),1):##the xy sum 
        sum_xy += x[index]*y[index]

    meanx = sum_x / n
    meany =sum_y / n
    
    ##b = (sum_xy-((sum_x * sum_y)/n))/(sum_x2 - (sum_x2/n))
    ##a = (sum_y/n) - (b*(sum_x/n))
    top = 0
    bot = 0
    for index in range (0,len(x),1):
        top += (x[index]-meanx)*(y[index]-meany)
        bot += (x[index]-meanx)**2
    b = top / bot
    a = meany - (b*meanx)


    ## corefficient of determination

    topSum = 0
    botSum = 0
    avey = arrAverage(y)
    for index in range (0, len(x),1):
        topSum += (y[index] - liniarReg(a,b,x[index]))**2
        botSum += (y[index] - avey)**2
    R2 = 1 - (topSum/botSum)
    R = math.sqrt(R2)## correlation
    
    return (a,b,R)


def liniarReg(a,b,x):
    haty = a + (b*x)
    return (haty)


def arrayDiff(array):## This perfroms cheating differentiation on the entire array and returns an array, given time step is 1
    change = []
    for index in range (0, len(array)-1,1):
        change += [gradTwo([index, array[index]],[index+1, array[index+1]])]
    return (change)








   
