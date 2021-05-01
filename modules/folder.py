# Modul ini digunakan untuk memanipulasi file dan/atau folder

import os
import sys
    
def copyFolder(oldDir, newDir):
    if not os.path.exists(newDir):
        os.makedirs(newDir)
        for (root,dirs,files) in os.walk(oldDir, topdown=True):

            if root == oldDir:
                for i in files:
                    f = open('\\'.join([oldDir, i]), 'r')
                    data = f.readlines()
                    f.close() 
                    f = open('\\'.join([newDir, i]), 'w')
                    f.writelines(data)
                    f.close()
            

def saveFolderValidator(saveName, saveRoot):
    if saveName not in os.listdir(saveRoot):
        comm = input("Folder tidak ditemukan, buat folder save baru ? [y/n]\n> ").strip().lower()
        if comm == 'y':
            while True:
                folderName = input("Masukkan nama folder untuk save: ").strip()
                if folderName.isalnum() and folderName.lower() != 'con':
                    break 
                else:
                    print("Nama folder tidak valid, ulangi")
            newFolder = '\\'.join([saveRoot, folderName])
            tempFolder = '\\'.join([saveRoot, 'temp'])
            start = '\\'.join([saveRoot, "start"])

            copyFolder(start, newFolder)
            return folderName 
        
        elif comm != 'n':
            print("Command tidak valid")
            sys.exit()
        else:
            sys.exit()
    else:
        return saveName

def removeDir(pathToDir):
    if os.path.exists(pathToDir):
        for (root,dirs,files) in os.walk(pathToDir):
            for i in files:
                os.remove('\\'.join([root, i]))
        os.rmdir(pathToDir)

def save(baseDir):
    tempDirectory = '\\'.join([baseDir, 'savefiles\\temp'])
    while True:
        newDirectory = input("\nMasukkan nama folder penyimpanan: ").strip()
        if not newDirectory.isalnum():
            print("\n[ERROR] : Nama folder hanya boleh berisi angka atau/dan huruf")
        elif newDirectory.lower() == "start":
            print("\n[ERROR] : Tidak diperbolehkan menyimpan pada folder start/")
        elif newDirectory.lower() == "temp":
            print("\n[ERROR] : Tidak diperbolehkan menyimpan pada folder temp/")
        else:
            break
    nama = newDirectory
    newDirectory = '\\'.join([baseDir, 'savefiles', newDirectory])

    removeDir(newDirectory)
    copyFolder(tempDirectory, newDirectory)
    print("\nSaving...")
    print("Data telah disimpan pada folder '%s'\n" %nama)

def exits(baseDir):
    tempPath = '\\'.join([baseDir, 'savefiles\\temp'])
    saveAtauTidak = input("\nApakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
    if saveAtauTidak.strip().lower() == 'y': 
        save(baseDir)
    elif saveAtauTidak.strip().lower() == 'n':
        pass
    else:
        print("\nCommand tidak dikenali, program akan keluar tanpa menyimpan\n")
    removeDir(tempPath)
    sys.exit()