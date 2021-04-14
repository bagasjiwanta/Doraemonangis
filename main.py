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
    inventory = os.path.join(sys.path[0], 'savefiles/%s/inventory.csv' %workname)

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
        
        elif command.lower().strip() == "login":
            userID, userRole, IDnum = access.login(userFiles)

        elif command.lower().strip() =="carirarity":
            cari.cari("rarity",gadgets)

        elif command.lower().strip() == "caritahun":
            cari.cari("tahun",gadgets)

        elif command.lower().strip() == "tambahitem":
            edit.tambah(userRole,consumables,gadgets)
        
        elif command.lower().strip() == "hapusitem":
            edit.hapus(userRole, consumables, gadgets, inventory)
        
        elif command.lower().strip() == "ubahjumlah":
            edit.jumlah(userRole,consumables,gadgets)
        
        elif command.lower().strip() == "pinjam":
            trx.pinjamambil(userRole, IDnum ,"gadget",gadgets,gadgetBorHis,inventory)

        elif command.strip().lower() == "kembalikan":
            trx.kembali(userRole, IDnum, inventory, gadgets, gadgetRetHis)

        elif command.lower().strip() == "minta":
            trx.pinjamambil(userRole, IDnum,"consumable",consumables,consumablesHis,inventory)

        elif command.lower().strip() == "riwayatpinjam":
            trx.history(userRole, "pinjam", userFiles, gadgets, consumables, gadgetRetHis, gadgetBorHis, consumablesHis)

        elif command.lower().strip() == "riwayatkembali":
            trx.history(userRole, "kembali", userFiles, gadgets, consumables, gadgetRetHis, gadgetBorHis, consumablesHis)

        elif command.lower().strip() == "riwayatambil":
            trx.history(userRole, "ambil", userFiles, gadgets, consumables, gadgetRetHis, gadgetBorHis, consumablesHis)
        
        # elif command.strip().lower() == "save":
        else:
            print("command tidak dikenali, coba lagi")
