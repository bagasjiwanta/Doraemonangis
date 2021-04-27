# Modul ini digunakan untuk mengubah jumlah, hapus item, dan menambah item

from modules import parser
from .parser import openParse, appendParse, writeParse, combineParse

def tambah(userRole,consumListCsv, gadgetListCsv):
    listgadgets = parser.openParse(gadgetListCsv)
    listconsum = parser.openParse(consumListCsv)
    continueinput=True
    if userRole=="admin":
        itemID=input("\nMasukan ID: ").strip()  #id item divalidasi terlebih dahulu
        if itemID[0]=="G":
            validGadgetID=True
            validConsumID=False
            for i in range(len(listgadgets)):
                if listgadgets[i][0]==itemID:
                    print("\nGagal menambahkan item karena ID sudah ada.\n")
                    continueinput=False
        elif itemID[0]=="C":
            validConsumID=True
            validGadgetID=False
            for i in range(len(listconsum)):
                if listconsum[i][0]==itemID:
                    print("\nGagal menambahkan item karena ID sudah ada.\n")
                    continueinput=False
        else:
            continueinput=False
            print("\nGagal menambahkan item karena ID tidak valid.\n")

        if continueinput:
            nama=input("Masukan Nama: ")
            deskripsi=input("Masukan Deskripsi: ")
            jumlah=input("Masukan Jumlah: ")
            if jumlah.isnumeric()==True:
                jumlahnum=int(jumlah)
            else:
                jumlahnum=0
            if jumlahnum<0 or jumlah.isnumeric()==False:
                print("\nInput jumlah tidak valid!\n")
            else:
                rarity=input("Masukan Rarity: ")
                validRarity=["S","A","B","C"]
                if rarity in validRarity:
                    #untuk consumable input hanya sampai rarity
                    if validConsumID:
                        newConsum = ';'.join([itemID, nama, deskripsi, jumlah, rarity])
                        appendParse(newConsum, consumListCsv)
                        print("\nItem telah berhasil ditambahkan ke database.\n")
                    
                    #untuk gadget input akan dilanjutkan sampai tahun
                    if validGadgetID:
                        tahun=int(input("Masukan tahun ditemukan: "))
                        if tahun<=0:
                            print("Input tahun tidak valid!")
                        else: #lulus semua syarat
                            newGadget = ';'.join([itemID, nama, deskripsi, jumlah, rarity, str(tahun)])
                            appendParse(newGadget, gadgetListCsv)
                            print("\nItem telah berhasil ditambahkan ke database.\n")
                else:
                    print("\nInput rarity tidak valid!\n")
    else:
        print("\nAnda tidak memiliki akses untuk menambah item\nSilakan login sebagai admin\n")

def hapus(userRole, consumListCsv, gadgetListCsv, inventoryCsv):
    listinventory=parser.openParse(inventoryCsv)
    if userRole == "admin":
        itemID=input("\nMasukkan ID item: ")
        if itemID[0]=="G":
            itemList=parser.openParse(gadgetListCsv)
            itemListCsv=gadgetListCsv
        elif itemID[0]=="C":
            itemList=parser.openParse(consumListCsv)
            itemListCsv=consumListCsv
        for i in range (len(itemList)):
            if itemList[i][0] == itemID:
                caution = input(f"Apakah anda yakin ingin menghapus {itemList[i][1]} (Y/N)? ")
                if caution.lower() == 'y':
                    itemList.pop(i) #menghapus item dari database gadget/consumables
                    writeParse(combineParse(itemList), itemListCsv)
                    print(f"\nItem tersebut telah berhasil dihapus dari database.\n")
                    #menghapus item dari inventory
                    for j in range(len(listinventory)):
                        if listinventory[j][1]==itemID:
                            listinventory.pop(j) #menghapus item dari database inventory
                            writeParse(combineParse(listinventory), inventoryCsv)
                    break
                else:
                    print() 
                    break 
        else: 
            print("\nTidak ada item dengan ID tersebut.\n")
    else:
        print("\nAnda tidak memiliki akses untuk menghapus item\nSilakan login sebagai admin\n")

def jumlah(userRole,consumListCsv, gadgetListCsv):
    listgadgets = parser.openParse(gadgetListCsv)
    listconsum = parser.openParse(consumListCsv)
    if userRole == "admin": #validasi role
        itemID=input("\nMasukkan ID: ").strip() 
        if itemID[0].strip() =="G":
            itemList=listgadgets
            itemListCsv=gadgetListCsv
        elif itemID[0].strip() == "C":
            itemList=listconsum
            itemListCsv=consumListCsv
        else: #validasi ID
            print("\nID tidak valid\n")
        notFound=True
        for i in range (len(itemList)): #pencarian item berdasarkan IDnya
            if itemList[i][0] == itemID:
                notFound=False
                jumlah=int(input("Masukan Jumlah: "))
                if jumlah>=0:
                    itemList[i][3]=str(int(itemList[i][3])+jumlah)
                    print(f"\n{jumlah} {itemList[i][1]} berhasil ditambahkan. Stok sekarang: {itemList[i][3]}\n")
                    writeParse(combineParse(itemList), itemListCsv)
                if jumlah<0:
                    if int(itemList[i][3])>((-1)*jumlah):
                        itemList[i][3]=str(int(itemList[i][3])+jumlah)
                        jumlah=jumlah*(-1)
                        print(f"\n{jumlah} {itemList[i][1]} berhasil dibuang. Stok sekarang: {itemList[i][3]}\n")
                        writeParse(combineParse(itemList), itemListCsv)
                    elif int(itemList[i][3])<((-1)*jumlah):
                        jumlah=jumlah*(-1)
                        print(f"\n{jumlah} {itemList[i][1]} gagal dibuang karena stok kurang. Stok sekarang: {itemList[i][3]} (<{jumlah})\n")
        if notFound:
            print("\nTidak ada item dengan ID tersebut!\n")
    else:
        print("\nAnda tidak memiliki akses untuk mengubah jumlah item\nSilakan login sebagai admin\n")