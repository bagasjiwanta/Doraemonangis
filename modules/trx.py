from .csvParser import openParse, appendParse, writeParse, combineParse

def pinjam(IDnum, itemID, itemList, itemListCsv, listpinjam, gadgetBorHisCsv):
    notFound=True
    for i in range (len(itemList)):
        if itemList[i][0] == itemID:
            notFound=False
            tanggal=input("Tanggal peminjaman: ")
            jumlah=int(input("Jumlah peminjaman: "))
            if jumlah<int(itemList[i][3]):
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
    
    
