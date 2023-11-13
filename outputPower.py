import pandas as pd
import matplotlib.pyplot as plt


rawPowerData = #deleted sensitive data
rawPowerData = rawPowerData[:500]

# the data
newData = {
    'Raw Power': rawPowerData
}
# create a data frame with the data from newData
newDataFrame = pd.DataFrame(newData)
# path of the Excel file
filePath = 'dataSheet2.xlsx'
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

plt.plot(rawPowerData, label='Raw Power')

plt.legend()

plt.title("Past Power Input")
plt.xlabel("Time")
plt.ylabel("Power")

plt.show()
