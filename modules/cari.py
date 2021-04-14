from modules import csvParser
from .csvParser import openParse

def cari(jenis,gadgets):
    listgadgets = csvParser.openParse(gadgets) #parsing file gadget.csv menjadi list
    listgadgets = listgadgets[1:] #menghapus header file
    if jenis=="rarity":
        rarity=input("Masukkan rarity: ")
        print("\nHasil pencarian:\n")
        for i in range (len(listgadgets)):
            if listgadgets[i][4]==rarity:
                print(f"Nama             : {listgadgets[i][1]}")
                print(f"Deskripsi        : {listgadgets[i][2]}")
                print(f"Jumlah           : {listgadgets[i][3]} buah")
                print(f"Rarity           : {listgadgets[i][4]}")
                print(f"Tahun Ditemukan  : {listgadgets[i][5]}\n")
    if jenis=="tahun":
        tahun=input("Masukkan tahun: ")
        kategori=input("Masukkan kategori: ")
        print("\nHasil pencarian:\n")
        for i in range (len(listgadgets)):
            if (kategori=="=" and listgadgets[i][5]==tahun) or (kategori==">" and listgadgets[i][5]>tahun) or (kategori=="<" and listgadgets[i][5]<tahun) or (kategori==">=" and listgadgets[i][5]>=tahun) or (kategori=="<=" and listgadgets[i][5]<=tahun):
                print(f"Nama             : {listgadgets[i][1]}")
                print(f"Deskripsi        : {listgadgets[i][2]}")
                print(f"Jumlah           : {listgadgets[i][3]} buah")
                print(f"Rarity           : {listgadgets[i][4]}")
                print(f"Tahun Ditemukan  : {listgadgets[i][5]}\n")
            