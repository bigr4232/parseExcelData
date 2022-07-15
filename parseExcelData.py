from audioop import avg
import pandas as pd
import os, glob, getopt, sys


if sys.argv[1] == "-f" and len(sys.argv) > 2:
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
    # print the content
    print('Content:')
    print(avgDF)
    print()

    avgDF.to_excel("output.xlsx")

else:
    print("Enter filename with argument -f [filename]")