import pandas as pd
import matplotlib.pyplot as plt

def makeListsTheSameLength (*lists):
    longestList = lists[0]
    for alist in lists:
        if len(alist) > len(longestList):
            longestList = alist

    for alist in lists:
        if len(alist) < len(longestList):
            while len(alist) < len(longestList):
                alist.append(alist[-1])

rawPowerData = #deleted sensitive data
forecast = #deleted sensitive data
outcome = #deleted sensitive data
makeListsTheSameLength(forecast, outcome)

# the data
newData = {
    'Forecast': forecast,
    'Outcome': outcome,
}
# create a data frame with the data from newData
newDataFrame = pd.DataFrame(newData)
# path of the Excel file
filePath = 'dataSheet.xlsx'
# sheet name of the existing data
sheetName = 'data'

# check if the Excel file exists. if not, create a new Excel file. If it does, append the data to the existing file.
try:
    existingData = pd.read_excel(filePath)
except FileNotFoundError:
    print("New Excel file made and data added to it.")
    newDataFrame.to_excel(filePath, sheet_name=sheetName, index=False)
else:
    combinedData = pd.concat([existingData, newDataFrame], ignore_index=True)
    combinedData.to_excel(filePath, index=False)
    print("Data appended to existing Excel file.")

plt.plot(forecast, label='Forecast')
plt.plot(outcome, label='Outcome')

plt.legend()

plt.title("Tomorrow's Data")
plt.xlabel("Time")
plt.ylabel("Power")

plt.show()
