import os 
import sys
import argparse 
from time import sleep 
from modules import csvParser
from modules import randomizer
from modules import access
from modules import cari
from modules import edit
from modules import trx
from modules import buatfolder



# id user dan role user (yang menggunakan sekarang)
userID = ''
userRole = ''
inventory = ''

if __name__=="__main__":
    commandParser = argparse.ArgumentParser(
    description="Kantong ajaib",
    usage="python kantongajaib.py nama_folder"
    )
    commandParser.add_argument("folder")
    commandParser = commandParser.parse_args()
    workdir = commandParser.folder.strip()
    workdir = buatfolder.saveFolderValidator(workdir, os.path.join(sys.path[0], 'savefiles/'))
    if workdir == '*':
        exit()
    else:
        buatfolder.copyFolder(os.path.join(sys.path[0], 'savefiles/%s/'%workdir), os.path.join(sys.path[0], 'savefiles/temp'))

    workdir = os.path.join(sys.path[0], 'savefiles/temp')
    workname = 'temp'
    # File dan struktur data 
    # Bentuk string, bisa langsung di parse dengan csvParser
    userFiles = os.path.join(sys.path[0], 'savefiles/%s/user.csv'%workname)
    gadgets = os.path.join(sys.path[0], 'savefiles/%s/gadget.csv'%workname)
    gadgetBorHis = os.path.join(sys.path[0], 'savefiles/%s/gadget_borrow_history.csv'%workname)
    gadgetRetHis = os.path.join(sys.path[0], 'savefiles/%s/gadget_return_history.csv'%workname)
    consumables = os.path.join(sys.path[0], 'savefiles/%s/consumable.csv'%workname)
    consumablesHis = os.path.join(sys.path[0], 'savefiles/%s/consumable_history.csv' %workname)


    print("\n---------------------\nSelamat datang di kantong ajaib\n"
    "---------------------\nMasukkan command")
    command = '' 

    while True:
        command = input("[%s:%s] > "%(userRole, userID))
        # list command dibawah sini
        if command.lower().strip() == "exit":
            exit()
            break 

        elif command.lower().strip() == "register":
            temp = access.register(userFiles, userRole)
            if temp != '':
                new = open(os.path.join(sys.path[0], '%s/inventory/%s.csv' %(workdir,temp)), 'w')
                new.write("id_gadget;nama_gadget;jumlah")
                new.close()
            

        elif command.lower().strip() == "login":
            userID, userRole, IDnum = access.login(userFiles)
            
            if userRole != "admin":
                if '.'.join([userID, 'csv']) in os.listdir(os.path.join(sys.path[0], 'src/')):
                    inventory = os.path.join(sys.path[0], '%s/inventory/%s.csv' %(workdir,userID))
                else:
                    print("Data inventory untuk user ini tidak tersedia (hilang), ingin membuat inventory baru? [y/n]")
                    confirm = input().strip().lower()
                    if confirm == 'y':         
                        new = open(os.path.join(sys.path[0], '%s/inventory/%s.csv' %userID), 'w')
                        new.write("id_gadget;nama_gadget;jumlah")
                        new.close()
                    print("Berhasil membuat inventory untuk user %s" %userID)


        elif command.lower().strip() =="carirarity":
            listgadgets = csvParser.openParse(gadgets)
            listconsum = csvParser.openParse(consumables)
            rarity=input("Masukkan rarity: ")
            cari.carirarity(rarity,listgadgets)

        elif command.lower().strip() == "caritahun":
            listgadgets = csvParser.openParse(gadgets)
            listgadgets = listgadgets[1:]
            tahun=input("Masukkan tahun: ")
            kategori=input("Masukkan kategori: ")
            cari.caritahun(tahun, kategori, listgadgets)

        elif command.lower().strip() == "tambahitem":
            listgadgets = csvParser.openParse(gadgets)
            listconsum = csvParser.openParse(consumables)
            if userRole=="admin":
                itemID=input("Masukan ID: ").strip()
                if itemID[0]=="G":
                    edit.tambahgadget(itemID, listgadgets, gadgets)
                elif itemID[0]=="C":
                    edit.tambahconsum(itemID, listconsum,consumables)
                else:
                    print("\nGagal menambahkan item karena ID tidak valid.")
            else:
                print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")
        
        elif command.lower().strip() == "hapusitem":
            listgadgets = csvParser.openParse(gadgets)
            listconsum = csvParser.openParse(consumables)
            if userRole == "admin":
                itemID=input("Masukkan ID: ").strip() 
                if itemID[0].strip() =="G":
                    edit.hapus(itemID, listgadgets, gadgets)
                elif itemID[0].strip() == "C":
                    edit.hapus(itemID, listconsum, consumables)
                else:
                    print("Tidak ada item dengan id Tersebut")
            else:
                print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")

        elif command.lower().strip() == "ubahjumlah":
            listgadgets = csvParser.openParse(gadgets)
            listconsum = csvParser.openParse(consumables)
            if userRole == "admin":
                itemID=input("Masukkan ID: ").strip() 
                if itemID[0].strip() =="G":
                    edit.jumlah(itemID, listgadgets, gadgets)
                elif itemID[0].strip() == "C":
                    edit.jumlah(itemID, listconsum, consumables)
                else:
                    print("Tidak ada item dengan id Tersebut")
            else:
                print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")
        
        elif command.lower().strip() == "pinjam":
            listgadgets = csvParser.openParse(gadgets)
            histpinjam = csvParser.openParse(gadgetBorHis)
            if userRole == "user":
                itemID=input("Masukkan ID item: ").strip() 
                trx.pinjam(IDnum, itemID, listgadgets, gadgets, histpinjam, gadgetBorHis, inventory)
            else:
                print("Silakan login sebagai user")

        elif command.lower().strip() == "minta":
            listconsum = csvParser.openParse(consumables)
            histconsum = csvParser.openParse(consumablesHis)
            if userRole == "user":
                itemID=input("Masukkan ID item: ").strip() 
                trx.pinjam(IDnum, itemID, listconsum, consumables, histconsum, consumablesHis, inventory)
            else:
                print("Silakan login sebagai user")

        elif command.lower().strip() == "riwayatpinjam":
            listgadgets = csvParser.openParse(gadgets)
            histpinjam = csvParser.openParse(gadgetBorHis)
            listuser = csvParser.openParse(userFiles)
            listgadgets=listgadgets[1:]
            histpinjam=histpinjam[1:]
            listuser=listuser[1:]
            jenis="pinjam"
            
            if userRole == "admin":
                trx.history(jenis,listuser,listgadgets, histpinjam)
            else:
                print("Silakan login sebagai admin")

        elif command.lower().strip() == "riwayatkembali":
            listgadgets = csvParser.openParse(gadgets)
            listuser = csvParser.openParse(userFiles)
            listkembali = csvParser.openParse(gadgetRetHis)
            listgadgets=listgadgets[1:]
            listkembali=listkembali[1:]
            listuser=listuser[1:]
            jenis="kembali"
            if userRole == "admin":
                trx.history(jenis,listuser,listgadgets, listkembali)
            else:
                print("Silakan login sebagai admin")

        elif command.lower().strip() == "riwayatambil":
            listconsum = csvParser.openParse(consumables)
            listuser = csvParser.openParse(userFiles)
            listambil = csvParser.openParse(consumablesHis)
            listconsum=listconsum[1:]
            listambil=listambil[1:]
            listuser=listuser[1:]
            jenis="ambil"
            if userRole == "admin":
                trx.history(jenis,listuser,listgadgets, listkembali)
            else:
                print("Silakan login sebagai admin")

        elif command.strip().lower() == "kembalikan":
            trx.kembalikan(IDnum, inventory, gadgets, gadgetRetHis)
        
        # elif command.strip().lower() == "save":


        else:
            print("command tidak dikenali, coba lagi")
