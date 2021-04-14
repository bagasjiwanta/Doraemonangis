import os
import sys
def initFolder(nama, pathKeFolder):
    os.mkdir(''.join([pathKeFolder, nama, '/']))
    newfolder = ''.join([pathKeFolder, nama, '/'])

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
            os.mkdir("/".join([newDir, 'inventory']))
            for j in files:
                print(j)
                f = open('\\'.join([oldDir, 'inventory', j]), 'r')
                data = f.readlines()
                f.close() 
                f = open('\\'.join([newDir, 'inventory', j]), 'w')
                f.writelines(data)
            break

def saveFolderValidator(saveName, saveRoot):
    if saveName not in os.listdir(saveRoot):
        print("Folder tidak ditemukan, buat folder save baru ? [y/n]")
        comm = input().strip().lower()
        if comm == 'y':
            while True:
                folderName = input("Masukkan nama folder untuk save: ").lower().strip()
                for i in folderName:
                    if not i.isalnum():
                        print("input folder tidak valid")
                        break
                else:
                    break

            initFolder(folderName, saveRoot)
            return folderName
        elif comm != 'n':
            print("Command tidak valid")
            return '*'
            exit
        else:
            return '*'
    else:
        return saveName