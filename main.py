import os 
import sys
from time import sleep 
from modules import csvParser
from modules import randomizer
from modules import access

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
        if command.lower() == "exit":
            exit
            break 

        elif command.lower() == "register":
            access.register(userFiles, userRole)

        elif command.lower() == "login":
            userID, userRole = access.login(userFiles)
        
        elif command.lower() =="carirarity":
            listgadgets=csvParser.openParse(gadgets)
            rarity=input("Masukkan rarity: ")
            print("\nHasil pencarian:\n")
            for i in range (len(listgadgets)):
                if listgadgets[i][4]==rarity:
                    print("Nama: %s"%listgadgets[i][1])
                    print("Deskripsi: %s"%listgadgets[i][2])
                    print("Jumlah: %s"%listgadgets[i][3])
                    print("Rarity: %s"%listgadgets[i][4])
                    print("Tahun Ditemukan: %s"%listgadgets[i][5])
                    print()
        else:
            print("command tidak dikenali, coba lagi")
    
       