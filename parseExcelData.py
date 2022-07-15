import pandas as pd
import os, glob, sys

# assign arguments
output = ""
path = ""
for i in range(len(sys.argv)):
    if sys.argv[i] == "-f":
        path = sys.argv[i+1]
    elif sys.argv[i] == "-o":
        if sys.argv[i+1][-5:] == ".xlsx":
            output = sys.argv[i+1]
        else:
            output = sys.argv[i + 1] + ".xlsx"
        


if os.path.exists(path):
    # use glob to get all the xlsx files in directory
    path = sys.argv[2]
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    avgDF = pd.DataFrame()
    # loop over the list of xlsx files
    counter = 0
    for f in csv_files:
        
        # read the xlsx file
        df = pd.read_excel(f)
        counter += 1

        if avgDF.empty:
            avgDF = df
        else:    
            avgDF.iloc[:,1:len(df.columns)] = avgDF.iloc[:,1:len(df.columns)].add(df.iloc[:,1:len(df.columns)])

    avgDF.iloc[:,1:len(avgDF.columns)] = avgDF.iloc[:,1:len(avgDF.columns)].div(counter)
    if output == "":
        avgDF.to_excel("output.xlsx")
    else:
        avgDF.to_excel(output)

else:
    print("Enter filename with argument -f [filename]")