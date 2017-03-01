from os import listdir
from os.path import isfile, join
mypath = "pdfTxt"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print onlyfiles[:50]
prevLine = ''
index = 0
for file in onlyfiles:
    with open(file) as f:

        index += 1
        if index == 1:
            prevLine = f.readline()
            continue
        currLine = f.readline()
        print prevLine, '|||', currLine
        outputFile.write(prevLine + '\n' if currLine[:-1] == '-' else '')

        prevLine = currLine


    #lines = [line if line[:-1] == "-" else " " for line in context ]
    #for line in context:
    #    if line[:-1] == "-":


