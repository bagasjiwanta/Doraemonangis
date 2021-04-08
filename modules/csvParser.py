def splitLine(listToSplit):
    a, b = 0, 0
    outputList = []
    while b < len(listToSplit):
        parts = '' 

        if listToSplit[b] == ';':
            parts = listToSplit[a:b]
            a = b + 1   
            outputList.append(parts)

        elif listToSplit[b:b+2] == '\n':
            parts = listToSplit[a:b]
            outputList.append(parts)

        elif b == len(listToSplit) - 1:
            parts = listToSplit[a:b+1]
            outputList.append(parts)

        b += 1   
    return outputList  

def openParse(inputCsv):
    csvData = open(inputCsv,'r').readlines()
    csvDataLength = len(csvData)
    outputCsv = [[0] for i in range(csvDataLength)]

    for i in range(csvDataLength):
        outputCsv[i] = splitLine(csvData[i])
    return outputCsv
        
def writeParse(inputData, csvToWrite):
    csvData = open(inputData, 'w')
    csvData.writelines(inputData)
    csvData.close()

def appendParse(inputLine, csvToWrite):
    csvData = open(csvToWrite, "a")
    csvData.write("\n")
    csvData.write(inputLine)
    csvData.close()
    