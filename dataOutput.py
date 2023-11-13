import pandas as pd

# the data
newData = {
    'Power': #sensitive data deleted
    'Power diff': #sensitive data deleted
    'Power diff 2': #sensitive data deleted
    
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
    combinedData = pd.concat([existingData, newDataFrame], ignore_index=True)
    combinedData.to_excel(filePath, index=False)
    print("Data appended to existing Excel file.")
except FileNotFoundError:
    print("New Excel file made and data added to it.")
    newDataFrame.to_excel(filePath, sheet_name=sheetName, index=False)
