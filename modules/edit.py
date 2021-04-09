from .csvParser import openParse, appendParse

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


