import os 
import sys
from time import sleep 
from modules import csvParser
from modules import randomizer
from modules import access
from modules import cari
from modules import edit
from modules import trx

# File dan struktur data 
# Bentuk string, bisa langsung di parse dengan csvParser
userFiles = os.path.join(sys.path[0], 'src/user.csv')
gadgets = os.path.join(sys.path[0], 'src/gadget.csv')
gadgetBorHis = os.path.join(sys.path[0], 'src/gadget_borrow_history.csv')
gadgetRetHis = os.path.join(sys.path[0], 'src/gadget_return_history.csv')
consumables = os.path.join(sys.path[0], 'src/consumable.csv')
consumablesHis = os.path.join(sys.path[0], 'src/consumable_history.csv')
# end of Files & Data Structure 

#parsing csv to list

# GUI section 
# end of GUI section 

# id user dan role user (yang menggunakan sekarang)
userID = ''
userRole = ''

if __name__=="__main__":

    # ini harusnya masuk ke GUI sih tpi tolong dong dibikinin nanti GUI nya 
    # gw nggak ngide mau gimana :( 
    sleep(0)
    print("\n---------------------\nSelamat datang di kantong ajaib\n"
    "---------------------\nMasukkan command")
    command = '' 
    sleep(0)
    # 

    while True:
        command = input("[%s:%s] > "%(userRole, userID))
        # list command dibawah sini
        if command.lower().strip() == "exit":
            exit
            break 

        elif command.lower().strip() == "register":
            access.register(userFiles, userRole)

        elif command.lower().strip() == "login":
            userID, userRole, IDnum = access.login(userFiles)
            
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
                trx.pinjam(IDnum, itemID, listgadgets, gadgets, histpinjam, gadgetBorHis)
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

        else:
            print("command tidak dikenali, coba lagi")
    
       