# important libraries
from os import path as ospath 
from sys import path as syspath
from sys import exit as keluar
from modules import access
from modules import edit
from modules import trx
from modules import parser
from modules import folder 
from modules import others

# username, userrole, dan userid yang menggunakan sekarang
userName = ''
userRole = ''
userID = ''

# File dan struktur data 
BASE_DIR = syspath[0]
userFiles = ospath.join(BASE_DIR, 'savefiles\\temp\\user.csv')
gadgets = ospath.join(BASE_DIR, 'savefiles\\temp\\gadget.csv')
gadgetBorHis = ospath.join(BASE_DIR, 'savefiles\\temp\\gadget_borrow_history.csv')
gadgetRetHis = ospath.join(BASE_DIR, 'savefiles\\temp\\gadget_return_history.csv')
consumables = ospath.join(BASE_DIR, 'savefiles\\temp\\consumable.csv')
consumablesHis = ospath.join(BASE_DIR, 'savefiles\\temp\\consumable_history.csv' )
inventory = ospath.join(BASE_DIR, 'savefiles\\temp\\inventory.csv')

if __name__=="__main__":
    parser.inputCli(BASE_DIR)

    print("\n---------------------\nSelamat datang di kantong ajaib\n"
    "---------------------\nMasukkan command")
    
    while True:
        command = input("[%s:%s] > "%(userRole, userName))

        # list command dibawah sini
        if command.lower().strip() == "exit":
            folder.exits(BASE_DIR)

        elif command.lower().strip() == "register":
            temp = access.register(userFiles, userRole)
        
        elif command.lower().strip() == "login":
            userName, userRole, userID = access.login(userFiles, userID, userName, userRole)

        elif command.lower().strip() =="carirarity":
            trx.cari("rarity",gadgets)

        elif command.lower().strip() == "caritahun":
            trx.cari("tahun",gadgets)

        elif command.lower().strip() == "tambahitem":
            edit.tambah(userRole,consumables,gadgets)
        
        elif command.lower().strip() == "hapusitem":
            edit.hapus(userRole, consumables, gadgets, inventory)
        
        elif command.lower().strip() == "ubahjumlah":
            edit.jumlah(userRole,consumables,gadgets)
        
        elif command.lower().strip() == "pinjam":
            trx.pinjamambil(userRole, userID ,"gadget",gadgets,gadgetBorHis,inventory)

        elif command.lower().strip() == "kembalikan":
            trx.kembali(userRole, userID, gadgets, inventory, gadgetRetHis)

        elif command.lower().strip() == "minta":
            trx.pinjamambil(userRole, userID,"consumable",consumables,consumablesHis,inventory)

        elif command.lower().strip() == "riwayatpinjam":
            trx.history(userRole, "pinjam", userFiles, gadgets, gadgetBorHis)

        elif command.lower().strip() == "riwayatkembali":
            trx.history(userRole, "kembali", userFiles, gadgets, gadgetRetHis)

        elif command.lower().strip() == "riwayatambil":
            trx.history(userRole, "ambil", userFiles, consumables, consumablesHis)
        
        elif command.lower().strip() == "save":
            folder.save(BASE_DIR)

        elif command.lower().strip() == "help":
            others.helper(userRole)
               
        else:
            print("command tidak dikenali, coba lagi")
