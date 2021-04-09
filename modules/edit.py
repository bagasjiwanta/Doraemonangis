from .csvParser import openParse, appendParse, writeParse, combineParse

def tambahgadget(itemID, listgadgets, gadgetListCsv):
    validID=True
    for i in range(len(listgadgets)):
        if listgadgets[i][0]==itemID:
            validID=False
            print("Gagal menambahkan item karena ID sudah ada")

    if validID:
        nama=input("Masukan Nama             : ")
        deskripsi=input("Masukan Deskripsi        : ")
        jumlah=int(input("Masukan Jumlah           : "))
        if jumlah<0:
            print("Input jumlah tidak valid!")
        else:
            jumlah=str(jumlah)
            rarity=input("Masukan Rarity           : ")
            validRarity=["S","A","B","C"]
            if rarity in validRarity:
                tahun=int(input("Masukan tahun ditemukan  : "))
                if tahun<=0:
                    print("Input tahun tidak valid!")
                else: #lulus semua syarat
                    tahun=str(tahun)
                    newGadget = ';'.join([itemID, nama, deskripsi, jumlah, rarity, tahun])
                    appendParse(newGadget, gadgetListCsv)
                    print("Item telah berhasil ditambahkan ke database.")

            else:
                print("Input rarity tidak valid!")

def tambahconsum(itemID, listconsum, consumListCsv):
    validID=True
    for i in range(len(listconsum)):
        if listconsum[i][0]==itemID:
            validID=False
            print("Gagal menambahkan item karena ID sudah ada")

    if validID:
        nama=input("Masukan Nama             : ")
        deskripsi=input("Masukan Deskripsi        : ")
        jumlah=int(input("Masukan Jumlah           : "))
        if jumlah<0:
            print("Input jumlah tidak valid!")
        else:
            jumlah=str(jumlah)
            rarity=input("Masukan Rarity           : ")
            validRarity=["S","A","B","C"]
            if rarity in validRarity:
                newConsum = ';'.join([itemID, nama, deskripsi, jumlah, rarity])
                appendParse(newConsum, consumListCsv)
                print("Item telah berhasil ditambahkan ke database.")
            else:
                print("Input rarity tidak valid!")

def hapus(itemID, itemList, itemListCsv):
    index = 0
    for i in itemList:
        if i[0] == itemID:
            caution = input("Apakah anda yakin ingin menghapus %s (Y/N)? "%(i[1]))
            if caution.lower() == 'y':
                itemList.remove(i)
                writeParse(combineParse(itemList), itemListCsv)
                print("Item tersebut telah berhasil dihapus dari database")
                break
            else: 
                break 
             
    else: 
        print("\nTidak ada item dengan ID tersebut.")

def jumlah(itemID, itemList, itemListCsv):
    notFound=True
    for i in range (len(itemList)):
        if itemList[i][0] == itemID:
            notFound=False
            jumlah=int(input("Masukan Jumlah: "))
            if jumlah>=0:
                itemList[i][3]=str(int(itemList[i][3])+jumlah)
                print("%d %s berhasil ditambahkan. Stok sekarang: %s"%(jumlah, itemList[i][1],itemList[i][3]))
                writeParse(combineParse(itemList), itemListCsv)
            if jumlah<0:
                if int(itemList[i][3])>((-1)*jumlah):
                    itemList[i][3]=str(int(itemList[i][3])+jumlah)
                    print("%d %s berhasil dibuang. Stok sekarang: %s"%((-1)*jumlah, itemList[i][1],itemList[i][3]))
                    writeParse(combineParse(itemList), itemListCsv)
                elif int(itemList[i][3])<((-1)*jumlah):
                    print("%d %s gagal dibuang karena stok kurang. Stok sekarang: %s (<%d)"%((-1)*jumlah, itemList[i][1],itemList[i][3],(-1)*jumlah))
    if notFound:
        print("Tidak ada item dengan ID tersebut!")
