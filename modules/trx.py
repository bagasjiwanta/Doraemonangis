from modules import parser
from modules import others
from .parser import openParse, appendParse, writeParse, combineParse

def pinjamambil(userRole, IDnum, jenis, itemListCsv, itemHisCsv, inventoryCsv):
    itemList = parser.openParse(itemListCsv)
    listinventory = parser.openParse(inventoryCsv)
    listpinjam = parser.openParse(itemHisCsv)
    if userRole == "user":
        itemID=input("Masukkan ID item: ").strip() 
        notFound=True #asumsi item tidak ditemukan
        for i in range (len(itemList)):
            if itemList[i][0] == itemID: #item ditemukan
                notFound=False
                if itemID[0] == "C" and itemID[1:].isnumeric(): #validasi prefiks item
                    tanggal=input("Tanggal permintaan (DD/MM/YYYY): ")
                    jumlah=int(input("Jumlah permintaan: "))
                    key = "minta"

                elif itemID[0] == "G" and itemID[1:].isnumeric(): #validasi prefiks item
                    tanggal=input("Tanggal peminjaman (DD/MM/YYYY): ")
                    jumlah=int(input("Jumlah peminjaman: "))
                    key = "pinjam"

                if jumlah<=int(itemList[i][3]): #mengecek apakah jumlah item cukup atau tidak
                    notfound_similar=True #asumsi item belum pernah dipinjam
                
                    for j in range (len(listinventory)): #mengecek apakah item sudah pernah dipinjam/ada di inventory
                        if listinventory[j][0]==IDnum and listinventory[j][1]==itemID: #mengecek ID user dengan ID item yang dimiliki
                            notfound_similar=False 
                            listinventory[j][3]=str(int(listinventory[j][3])+jumlah) #mengubah jumlah item yang telah pernah dipinjam/diambil 
                            writeParse(combineParse(listinventory), inventoryCsv) #parsing inventory dari matriks ke csv

                    if notfound_similar: #jika item belum pernah pinjam/ambil maka akan dibuat baris baru 
                        newinventory = ';'.join([IDnum, itemID, itemList[i][1],str(jumlah),itemList[i][4]])
                        appendParse(newinventory, inventoryCsv)
                    
                    print(f"Item {itemList[i][1]} (x{jumlah}) berhasil di{key}!")

                    itemList[i][3]=str(int(itemList[i][3])-jumlah) #jumlah item yang tersedia berkurang
                    writeParse(combineParse(itemList), itemListCsv) #parsing list item dari matriks ke csv

                    IDpinjam=str(len(listpinjam)) #buat ID pinjam/ambil
                    newpinjam = ';'.join([IDpinjam, IDnum, itemID, tanggal, str(jumlah)]) 
                    appendParse(newpinjam, itemHisCsv) #menambahkan baris baru pada history peminjaman/pengambilan
                else: #jumlah item kurang
                    print(f"Stok {jenis} kurang")
        if notFound: #item tidak ditemukan
            print("Tidak ada item dengan ID tersebut!")
    else:
        print("Silakan login sebagai user")

def kembali(userRole, IDnum, itemListCsv, inventoryCsv, gadgetRetHisCsv):
    itemList = parser.openParse(itemListCsv)
    listinventory = parser.openParse(inventoryCsv)
    listkembali= parser.openParse(gadgetRetHisCsv)

    if userRole == "user":
        count=0 #penghitung urutan inventory
        urutan=["" for i in range (len(itemList))]
        for i in range (len(listinventory)): #pengecekan isi inventory yang ingin dikembalikan
            if listinventory[i][0]==IDnum and listinventory[i][1][0]=="G" and listinventory[i][3]!="0":
                urutan[count]=listinventory[i][2] #menyimpan data gadget yang dapat dikembalikan
                count+=1
                print(f"{count}. {listinventory[i][2]} (x{listinventory[i][3]})")
        nomorpinjam=int(input("Masukan nomor peminjaman: "))
        tanggalkembali=input("Tanggal pengembalian (DD/MM/YYYY): ")
        jumlahkembali=int(input("Masukan jumlah pengembalian: "))

        for i in range (len(listinventory)): #pengubahan jumlah inventory
            if ((listinventory[i][0]==IDnum) and (listinventory[i][2]==urutan[nomorpinjam-1])) :
                itemID=listinventory[i][1]
                listinventory[i][3]=str(int(listinventory[i][3])-jumlahkembali) #jumlah gadget di inventory berkurang karena telah dikembalikan
                writeParse(combineParse(listinventory), inventoryCsv)

        for i in range (len(itemList)): #pengubahan jumlah gadget tersedia
            if itemList[i][1]==urutan[nomorpinjam-1]:
                itemList[i][3]=str(int(itemList[i][3])+jumlahkembali) #jumlah gadget bertambah sebanyak jumlah yang dikembalikan
                writeParse(combineParse(itemList), itemListCsv)

        IDkembali=str(len(listkembali))
        newkembali = ';'.join([IDkembali, IDnum, itemID, tanggalkembali, str(jumlahkembali)])
        appendParse(newkembali, gadgetRetHisCsv) #penambahan baris pada history pengembalian gadget

        print(f"\nItem {urutan[nomorpinjam-1]} (x{jumlahkembali}) telah dikembalikan.")
    else:
        print("Silakan login sebagai user")

def history(userRole, jenis, userCsv, itemListCsv, itemHisCsv):
    if userRole == "admin":
        listuser=parser.openParse(userCsv)
        itemList=parser.openParse(itemListCsv)
        listhistory=parser.openParse(itemHisCsv)

        #menghilangkan header pada matrix agar dapat dilakukan operasi sorting

        listuser=listuser[1:]
        itemList=itemList[1:]
        listhistory=listhistory[1:]
        #menyocokkan dengan jenis riwayat 
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
        sortedtanggal=[[0 for i in range (2)] for j in range (len(listhistory))]
        for i in range (len(listhistory)):
            sortedtanggal[i][0]=int(listhistory[i][3][6]+listhistory[i][3][7]+listhistory[i][3][8]+listhistory[i][3][9]+listhistory[i][3][3]+listhistory[i][3][4]+listhistory[i][3][0]+listhistory[i][3][1])
            sortedtanggal[i][1]=int(listhistory[i][0]) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"\nMenampilkan 5 riwayat {phrase1} terbaru\n")

        for i in range (banyakdata):
            for j in range (len(listhistory)):
                if listhistory[j][0]==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"ID {phrase1}: {listhistory[j][0]}")
                    for k in range (len(listuser)): #mencocokkan nama peminjam
                        if listuser[k][0]==listhistory[j][1]:
                            print(f"Nama {phrase2}: {listuser[k][2]}")
                    for l in range (len(itemList)):
                        if itemList[l][0]==listhistory[j][2]: #mencocokkan nama gadget
                            print(f"Nama {phrase3}: {itemList[l][1]}")
                    print(f"Tanggal {phrase1}: {listhistory[j][3]}")
                    print(f"Jumlah: {listhistory[j][4]}")
            print()
            if (i%5==4):
                lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break

    else:
        print("Silakan login sebagai admin")       

def cari(jenis,gadgets):
    listgadgets = parser.openParse(gadgets)[1:] #parsing file gadget.csv menjadi list
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
            