import pandas as pd

# the data
newData = {
    'Power': [2398.0, 2345.5, 2137.0, 4064.0, 3249.0, 2476.5, 2659.5, 686.0, 541.5, 1124.0, 967.5, 1206.0, 1256.0, 956.0, 1291.5, 2646.5, 4417.5, 3065.0, 1325.5, 1011.0, 4802.5, 586.5, 5301.5, 2137.0, 2139.0, 2210.0, 1350.0, 486.5, 517.5, 566.5, 642.5, 552.0, 640.5, 772.0, 2223.5, 621.0, 679.5, 798.0, 622.0, 746.0, 691.0, 2213.5, 2255.5, 2279.5, 2796.5, 2597.5, 630.0, 604.0],
    'Power diff': [-52.5, -208.5, 1927.0, -815.0, -772.5, 183.0, -1973.5, -144.5, 582.5, -156.5, 238.5, 50.0, -300.0, 335.5, 1355.0, 1771.0, -1352.5, -1739.5, -314.5, 3791.5, -4216.0, 4715.0, -3164.5, 2.0, 71.0, -860.0, -863.5, 31.0, 49.0, 76.0, -90.5, 88.5, 131.5, 1451.5, -1602.5, 58.5, 118.5, -176.0, 124.0, -55.0, 1522.5, 42.0, 24.0, 517.0, -199.0, -1967.5, -26.0],
    'Power diff 2': [-156.0, 2135.5, -2742.0, 42.5, 955.5, -2156.5, 1829.0, 727.0, -739.0, 395.0, -188.5, -350.0, 635.5, 1019.5, 416.0, -3123.5, -387.0, 1425.0, 4106.0, -8007.5, 8931.0, -7879.5, 3166.5, 69.0, -931.0, -3.5, 894.5, 18.0, 27.0, -166.5, 179.0, 43.0, 1320.0, -3054.0, 1661.0, 60.0, -294.5, 300.0, -179.0, 1577.5, -1480.5, -18.0, 493.0, -716.0, -1768.5, 1941.5],
    
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