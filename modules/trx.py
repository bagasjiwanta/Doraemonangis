from .csvParser import openParse, appendParse, writeParse, combineParse

def pinjam(IDnum, itemID, itemList, itemListCsv, listpinjam, history, inventories):
    notFound=True
    for i in range (len(itemList)):
        if itemList[i][0] == itemID:
            notFound=False
            if itemID[0] == "C":
                tanggal=input("Tanggal permintaan: ")
                jumlah=int(input("Jumlah permintaan: "))
                key = "minta"

            elif itemID[0] == "G":
                tanggal=input("Tanggal peminjaman: ")
                jumlah=int(input("Jumlah peminjaman: "))
                key = "pinjam"

            if jumlah<=int(itemList[i][3]):
                itemList[i][3] = str(int(itemList[i][3]) - jumlah)
                print("Item %s (x%d) berhasil di%s!"%(itemList[i][1], jumlah, key))
                writeParse(combineParse(itemList), itemListCsv)
                IDpinjam=str(len(listpinjam))
                newpinjam = ';'.join([IDpinjam, IDnum, itemID, tanggal, str(jumlah)])
                appendParse(newpinjam, history)
                
                if itemID[0] == 'G':
                    inventory = openParse(inventories)
                    for j in inventory:
                        if j[0] == itemID:
                            j[2] = str(int(j[2]) + jumlah) 
                            inventory = combineParse(inventory)
                            writeParse(inventory, inventories)
                            break

                    else: 
                        appendParse(';'.join([itemID, itemList[i][1],str(jumlah)]), inventories)
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


def kembalikan(userID, inventories, GadgetCsv, GadgetRetCsv):
    inventory = openParse(inventories)
    gadget = openParse(GadgetCsv)
    histReturn = openParse(GadgetRetCsv)
    index = 0

    print("\n--Inventory--")
    for i in range(1, len(inventory)):
        print("ID = %s \t%s (x%s)" %(inventory[i][0], inventory[i][1], inventory[i][2]))
    print("")
    no = input("Masukkan id gadget : ")

    for i in range(len(inventory)):
        if inventory[i][0] == no:
            index = i
            break
    else:
        print("Tidak ditemukan item dengan ide %s" %no)
        return 1
    
    tgl = input("Masukkan tanggal pengembalian : ")
    try:
        jml = int(input("Masukkan jumlah pengembalian: "))
    except ValueError:
        print("Jumlah invalid")
        return 1

    if jml < 0:
        print("Jumlah yang anda masukkan invalid")
        
    elif jml > int(inventory[index][2]):
        print("Jumlah yang anda masukkan lebih besar dari jumlah yang anda miliki")
        
    else:
        if jml == int(inventory[index][2]):
            inventory.pop(index)
           
        else:
            inventory[index][2] = str(int(inventory[index][2])-jml)
        print("Pengembalian sukses!")
        for i in gadget:
            if i[0] == no:
                i[3] = str(int(i[3]) + jml)
                break
        
        output = combineParse(gadget)
        writeParse(output, GadgetCsv)
        output = combineParse(inventory)
        writeParse(output, inventories)
        newhistory = ';'.join([str(len(histReturn)), userID, no, tgl, str(jml)])
        appendParse(newhistory, GadgetRetCsv)
