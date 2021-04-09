import os 
import sys
from time import sleep 
from modules import csvParser
from modules import randomizer
from modules import access
from modules import cari
from modules import edit
from modules import hapus 

# File dan struktur data 
# Bentuk string, bisa langsung di parse dengan csvParser
userFiles = os.path.join(sys.path[0], 'src/user.csv')
gadgets = os.path.join(sys.path[0], 'src/gadget.csv')
gadgetBorHis = os.path.join(sys.path[0], 'src/gadget_borrow_history.csv')
gadgetRetHis = os.path.join(sys.path[0], 'src/gadget_borrow_history.csv')
consumables = os.path.join(sys.path[0], 'src/consumable.csv')
consumablesHis = os.path.join(sys.path[0], 'src/consumable_history.csv')
# end of Files & Data Structure 

# GUI section 
# end of GUI section 

# id user dan role user (yang menggunakan sekarang)
userID = ''
userRole = ''

if __name__=="__main__":

    # ini harusnya masuk ke GUI sih tpi tolong dong dibikinin nanti GUI nya 
    # gw nggak ngide mau gimana :( 
    sleep(1)
    print("\n---------------------\nSelamat datang di kantong ajaib\n"
    "---------------------\nMasukkan command")
    command = '' 
    sleep(1)
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
            userID, userRole = access.login(userFiles)
        
        elif command.lower().strip() =="carirarity":
            listgadgets=csvParser.openParse(gadgets)
            rarity=input("Masukkan rarity: ")
            cari.carirarity(rarity,listgadgets)

        elif command.lower().strip() == "caritahun":
            listgadgets=csvParser.openParse(gadgets)
            tahun=input("Masukkan tahun: ")
            kategori=input("Masukkan kategori: ")
            cari.caritahun(tahun, kategori, listgadgets)

        elif command.lower().strip() == "tambahitem":
            if userRole=="admin":
                itemID=input("Masukan ID               : ").strip()
                if itemID[0]=="G":
                    listgadgets=csvParser.openParse(gadgets)
                    edit.tambahgadget(itemID, listgadgets, gadgets)
                elif itemID[0]=="C":
                    listconsum=csvParser.openParse(consumables)
                    edit.tambahconsum(itemID, listconsum,consumables)
                else:
                    print("\nGagal menambahkan item karena ID tidak valid.")
            else:
                print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")
        
        elif command.lower().strip() == "hapusitem":
            if userRole == "admin":
                itemID=input("Masukkan ID             : ").strip() 
                if itemID[0].strip() =="G":
                    listgadgets = csvParser.openParse(gadgets)
                    hapus.hapusgadget(itemID, listgadgets, gadgets)
                elif itemID[0].strip() == "C":
                    listconsum = csvParser.openParse(consumables)
                    hapus.hapusconsum(itemID, listconsum, consumables)
                else:
                    print("Tidak ada item dengan id Tersebut")
            else:
                print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")
        else:
            print("command tidak dikenali, coba lagi")
    
       