# Modul ini digunakan untuk memanipulasi file dan/atau folder

import os
import sys
def initFolder(nama, pathKeFolder):
    if not os.path.exists(''.join([pathKeFolder, nama, '\\'])):
        os.mkdir(''.join([pathKeFolder, nama, '\\']))
        newfolder = ''.join([pathKeFolder, nama, '\\'])

        f = open(''.join([newfolder, 'user.csv']), 'w')
        f.write("""id;username;nama;alamat;password;role
    000000;admin;-;-;admin;admin""")
        f.close
        
        f = open(''.join([newfolder, 'gadget.csv']), 'w')
        gadgets = [
            'id;nama;deskripsi;jumlah;rarity',
            'G1;Baling baling bambu;Bisa terbang;5;A',
            'G2;Pintu kemana saja;Mau kemana-mana tinggal gas;2;A',
            'G3;Kaca pembesar;Eh eh eh kok jadi besar;1;B',
            'G4;Kamera pengganti baju;Mau coba baju yang mana ? letsgo aja;5;C',
            'G5;Roti penerjemah;Belajar bahasa apa aja langsung bisa;10;C'
            ]
        f.writelines(gadgets)
        f.close() 

        f = open(''.join([newfolder, 'consumable.csv']), 'w')
        consumables = [
            'id;nama;deskripsi;jumlah;rarity'
            'C1;Dorayaki;Kesukaan doraemon;7;S',
            'C2;Sushi ikan;~Fresh from the sea~;10;B',
            'C3;Ayam goreng;Sedapnye ayam goreng;2;A',
            'C4;Donat JCO;Mainstream banget apalagi pas ultah temen;12;B'
        ]
        f.writelines(consumables)
        f.close() 

        f = open(''.join([newfolder, 'consumable_history.csv']), 'w')
        f.write('id;id_pengambil;id_consumable;tanggal_peminjaman')
        f.close()

        f = open(''.join([newfolder, 'gadget_borrow_history.csv']), 'w')
        f.write('id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah')
        f.close() 

        f = open(''.join([newfolder, 'gadget_return_history.csv']), 'w')
        f.write('id;id_peminjam;id_gadget;tanggal_pengembalian;jumlah')
        f.close() 

        os.mkdir(''.join([newfolder, 'inventory']))
    
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
            
            elif root == "".join([oldDir, 'inventory']):
                os.mkdir("\\".join([newDir, 'inventory']))
                for j in files:
                    f = open('\\'.join([oldDir, 'inventory', j]), 'r')
                    data = f.readlines()
                    f.close() 
                    f = open('\\'.join([newDir, 'inventory', j]), 'w')
                    f.writelines(data)
                break

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

            initFolder(folderName, saveRoot)

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
    newDirectory = input("Masukkan nama folder penyimpanan: ").strip()
    nama = newDirectory
    newDirectory = '\\'.join([baseDir, 'savefiles', newDirectory])

    removeDir(newDirectory)
    copyFolder(tempDirectory, newDirectory)
    print("sukses melakukan penyimpanan di folder '%s'" %nama)

def exits(baseDir):
    tempPath = '\\'.join([baseDir, 'savefiles\\temp'])
    removeDir(tempPath)
    sys.exit()