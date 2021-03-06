from argparse import ArgumentParser
import os.path as ospath
from . import folder
from sys import exit as keluar

def splitLine(listToSplit): # input line yang mau displit jadi list
    # makan;minum;saya;kamu;2002 → ['makan','minum','saya','kamu','2002']
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


def openParse(inputCsv):  # input string (path ke file csv)
    ''' Dari
    123;bagas;jiwanta;maxwell;bali
    makan;nasi;padang;bareng;bareng
        Menjadi
    ['123','bagas','jiwanta','maxwell','bali']
    ['makan','nasi','padang','bareng','bareng'] '''

    csvData = open(inputCsv,'r').readlines()
    csvDataLength = len(csvData)
    outputCsv = [[0] for i in range(csvDataLength)]
    for i in range(csvDataLength):
        outputCsv[i] = splitLine(csvData[i])
    return outputCsv


def combineParse(inputmatrix): #inputdata = matrix
    output = ''
    i = 0
    while i < len(inputmatrix) - 1:
        output += ";".join(inputmatrix[i]) + "\n"
        i += 1 
    output += ";".join(inputmatrix[i])
    return output 
        

def writeParse(inputData, csvToWrite): #inputData=string, csvToWrite=string(path ke file)
    # menulis ulang seluruh isi file csv 
    csvData = open(csvToWrite, 'w')
    csvData.writelines(inputData)
    csvData.close()


def appendParse(inputLine, csvToWrite): #inputLine=string(1 line), csvToWrite=string(path ke file)
    # menambah 1 line ke file csv
    csvData = open(csvToWrite, "a")
    csvData.write("\n")
    csvData.write(inputLine)
    csvData.close()


def inputCli(baseDir):
    commandParser = ArgumentParser(
    description="Kantong ajaib",
    usage="python kantongajaib.py nama_folder")
    
    commandParser.add_argument("folder")
    commandParser = commandParser.parse_args()
    workdir = commandParser.folder.strip()

    workdir = folder.saveFolderValidator(workdir, ospath.join(baseDir, 'savefiles\\'))
    print(workdir)
    if workdir == '*':
        keluar()
    elif ospath.exists('\\'.join([baseDir, 'savefiles\\temp'])):
        print("Ditemukan autosave sebelumnya, sepertinya program tidak terminate dengan benar sebelumnya"
        "\nApakah anda ingin menyimpan autosave sebelumnya ?[Y/N]")
        choice = input()
        if choice.strip().lower() == 'y':
            folder.save(baseDir)
    else:
        folder.copyFolder(ospath.join(baseDir, 'savefiles\\%s\\'%workdir), ospath.join(baseDir, 'savefiles\\temp'))