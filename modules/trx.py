from .csvParser import openParse, appendParse, writeParse, combineParse

def pinjam(IDnum, itemID, itemList, itemListCsv, listpinjam, gadgetBorHisCsv):
    notFound=True
    for i in range (len(itemList)):
        if itemList[i][0] == itemID:
            notFound=False
            tanggal=input("Tanggal peminjaman: ")
            jumlah=int(input("Jumlah peminjaman: "))
            if jumlah<=int(itemList[i][3]):
                itemList[i][3]=str(int(itemList[i][3])-jumlah)
                print("Item %s (x%d) berhasil dipinjam!"%(itemList[i][1],jumlah))
                writeParse(combineParse(itemList), itemListCsv)
                IDpinjam=str(len(listpinjam))
                newpinjam = ';'.join([IDpinjam, IDnum, itemID, tanggal, str(jumlah)])
                appendParse(newpinjam, gadgetBorHisCsv)
            else:
                print("Stok gadget kurang")
    if notFound:
        print("Tidak ada item dengan ID tersebut!")

def history(jenis,listuser, itemList, listtrx):
    if jenis == "pinjam":
        phrase1="Peminjaman"
        phrase2="Peminjam"
        phrase3="Gadget"
    elif jenis == "kembali":
        phrase1="Pengembalian"
        phrase2="Pengembali"
        phrase3="Gadget"
    elif jenis == "ambil":
        phrase1="Pengambilan"
        phrase2="Pengambil"
        phrase3="Consumable"
    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (len(listtrx))]
    for i in range (len(listtrx)):
        sortedtanggal[i][0]=int(listtrx[i][3][6]+listtrx[i][3][7]+listtrx[i][3][8]+listtrx[i][3][9]+listtrx[i][3][3]+listtrx[i][3][4]+listtrx[i][3][0]+listtrx[i][3][1])
        sortedtanggal[i][1]=int(listtrx[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    if len(sortedtanggal)>5:
        banyak=5
    else:
        banyak=len(sortedtanggal)
    for i in range (banyak):
        for j in range (len(listtrx)):
            if listtrx[j][0]==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print("ID %s       : %s"%(phrase1,listtrx[j][0]))
                for k in range (len(listuser)): #mencocokkan nama peminjam
                    if listuser[k][0]==listtrx[j][1]:
                        print("Nama %s       : %s"%(phrase2,listuser[k][2]))
                for l in range (len(itemList)):
                    if itemList[l][0]==listtrx[j][2]: #mencocokkan nama gadget
                        print("Nama %s         : %s"%(phrase3,itemList[k][1]))
                print("Tanggal %s  : %s"%(phrase1,listtrx[j][3]))
                print("Jumlah              : %s"%listtrx[j][4])
        print()



    
    
