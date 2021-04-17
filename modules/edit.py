# Modul ini digunakan untuk mengubah jumlah, hapus item, dan menambah item

from modules import parser
from .parser import openParse, appendParse, writeParse, combineParse

def tambah(userRole,consumListCsv, gadgetListCsv):
    listgadgets = parser.openParse(gadgetListCsv)
    listconsum = parser.openParse(consumListCsv)
    continueinput=True
    if userRole=="admin":
        itemID=input("Masukan ID: ").strip()  #id item divalidasi terlebih dahulu
        if itemID[0]=="G":
            validGadgetID=True
            validConsumID=False
            for i in range(len(listgadgets)):
                if listgadgets[i][0]==itemID:
                    print("Gagal menambahkan item karena ID sudah ada")
                    continueinput=False
        elif itemID[0]=="C":
            validConsumID=True
            validGadgetID=False
            for i in range(len(listconsum)):
                if listconsum[i][0]==itemID:
                    print("Gagal menambahkan item karena ID sudah ada")
                    continueinput=False
        else:
            print("\nGagal menambahkan item karena ID tidak valid.")

        if continueinput:
            nama=input("Masukan Nama: ")
            deskripsi=input("Masukan Deskripsi: ")
            jumlah=int(input("Masukan Jumlah: "))
            if jumlah<0:
                print("Input jumlah tidak valid!")
            else:
                jumlah=str(jumlah)
                rarity=input("Masukan Rarity: ")
                validRarity=["S","A","B","C"]
                if rarity in validRarity:
                    #untuk consumable input hanya sampai rarity
                    if validConsumID:
                        newConsum = ';'.join([itemID, nama, deskripsi, jumlah, rarity])
                        appendParse(newConsum, consumListCsv)
                        print("Item telah berhasil ditambahkan ke database.")
                    
                    #untuk gadget input akan dilanjutkan sampai tahun
                    if validGadgetID:
                        tahun=int(input("Masukan tahun ditemukan: "))
                        if tahun<=0:
                            print("Input tahun tidak valid!")
                        else: #lulus semua syarat
                            newGadget = ';'.join([itemID, nama, deskripsi, jumlah, rarity, str(tahun)])
                            appendParse(newGadget, gadgetListCsv)
                            print("Item telah berhasil ditambahkan ke database.")
                else:
                    print("Input rarity tidak valid!")
    else:
        print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin")

def hapus(userRole, consumListCsv, gadgetListCsv, inventoryCsv):
    listinventory=parser.openParse(inventoryCsv)
    if userRole == "admin":
        itemID=input("Masukkan ID item: ")
        if itemID[0]=="G":
            itemList=parser.openParse(gadgetListCsv)
            itemListCsv=gadgetListCsv
        elif itemID[0]=="C":
            itemList=parser.openParse(consumListCsv)
            itemListCsv=consumListCsv
        for i in range (len(itemList)):
            if itemList[i][0] == itemID:
                caution = input(f"Apakah anda yakin ingin menghapus {itemList[i][0]} (Y/N)? ")
                if caution.lower() == 'y':
                    itemList.pop(i) #menghapus item dari database gadget/consumables
                    writeParse(combineParse(itemList), itemListCsv)
                    print("Item tersebut telah berhasil dihapus dari database")
                    #menghapus item dari inventory
                    for j in range(len(listinventory)):
                        if listinventory[j][1]==itemID:
                            listinventory.pop(j) #menghapus item dari database inventory
                            writeParse(combineParse(listinventory), inventoryCsv)
                    break
                else: 
                    break 
        else: 
            print("\nTidak ada item dengan ID tersebut.")
    else:
        print("\nAnda tidak memiliki akses untuk menghapus item\nSilakan login sebagai admin")

def jumlah(userRole,consumListCsv, gadgetListCsv):
    listgadgets = parser.openParse(gadgetListCsv)
    listconsum = parser.openParse(consumListCsv)
    if userRole == "admin": #validasi role
        itemID=input("Masukkan ID: ").strip() 
        if itemID[0].strip() =="G":
            itemList=listgadgets
            itemListCsv=gadgetListCsv
        elif itemID[0].strip() == "C":
            itemList=listconsum
            itemListCsv=consumListCsv
        else: #validasi ID
            print("ID tidak valid")
        notFound=True
        for i in range (len(itemList)): #pencarian item berdasarkan IDnya
            if itemList[i][0] == itemID:
                notFound=False
                jumlah=int(input("Masukan Jumlah: "))
                if jumlah>=0:
                    itemList[i][3]=str(int(itemList[i][3])+jumlah)
                    print(f"{jumlah} {itemList[i][1]} berhasil ditambahkan. Stok sekarang: {itemList[i][3]}")
                    writeParse(combineParse(itemList), itemListCsv)
                if jumlah<0:
                    if int(itemList[i][3])>((-1)*jumlah):
                        itemList[i][3]=str(int(itemList[i][3])+jumlah)
                        jumlah=jumlah*(-1)
                        print(f"{jumlah} {itemList[i][1]} berhasil dibuang. Stok sekarang: {itemList[i][3]}")
                        writeParse(combineParse(itemList), itemListCsv)
                    elif int(itemList[i][3])<((-1)*jumlah):
                        jumlah=jumlah*(-1)
                        print(f"{jumlah} {itemList[i][1]} gagal dibuang karena stok kurang. Stok sekarang: {itemList[i][3]} (<{jumlah})")
        if notFound:
            print("Tidak ada item dengan ID tersebut!")
    else:
        print("\nAnda tidak memiliki akses untuk mengubah jumlah item\nSilakan login sebagai admin")