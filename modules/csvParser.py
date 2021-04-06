def lineSplit(listToSplit):
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
def parser(inputCsv):
    csvFile = open(inputCsv,'r')
    csvData = csvFile.readlines()
    csvDataLength = len(csvData)
    outputCsv = [[0] for i in range(csvDataLength)]

    for i in range(csvDataLength):
        outputCsv[i] = lineSplit(csvData[i])
    return outputCsv
        