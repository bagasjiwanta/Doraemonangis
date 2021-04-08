from .csvParser import openParse

def carirarity(rarity, listgadgets):
    print("\nHasil pencarian:\n")
    for i in range (len(listgadgets)):
        if listgadgets[i][4]==rarity:
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()

def caritahun(tahun, kategori, listgadgets):
    for i in range (len(listgadgets)):
        if kategori=="=" and listgadgets[i][5]==tahun and listgadgets[i][5]!="tahun_ditemukan":
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()
        if kategori==">" and listgadgets[i][5]>tahun and listgadgets[i][5]!="tahun_ditemukan":
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()
        if kategori=="<" and listgadgets[i][5]<tahun and listgadgets[i][5]!="tahun_ditemukan":
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()
        if kategori==">=" and listgadgets[i][5]>=tahun and listgadgets[i][5]!="tahun_ditemukan":
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()
        if kategori=="<=" and listgadgets[i][5]<=tahun and listgadgets[i][5]!="tahun_ditemukan":
            print("Nama             : %s"%listgadgets[i][1])
            print("Deskripsi        : %s"%listgadgets[i][2])
            print("Jumlah           : %s buah"%listgadgets[i][3])
            print("Rarity           : %s"%listgadgets[i][4])
            print("Tahun Ditemukan  : %s"%listgadgets[i][5])
            print()