# mengurus hal hal lain seperti validasi tanggal, membuat random number
import time 

def randomInt(digit): 
    # input digit = berapa digit integer random yang ingin dihasilkan
    # contoh : randomInt(8) = 12345678
    randstr = int(str(time.time() - int(time.time()))[2:digit+1]) 
    rvalue = int(time.strftime("%S", time.localtime()))
    return ("%d" % (rvalue*randstr))[:digit]


def validasiTanggal(tanggal):
    # tanggal dalam format DD/MM/YYYY
    if len(tanggal) != 10:
        print("\n[ERROR] : Tanggal tidak sesuai format")
        return False 

    listTanggal = []
    part = '' 
    for i in tanggal:
        if i != '/':
            part += i
        else:
            listTanggal.append(part)
            part = ''
    else:
        listTanggal.append(part)

    listTanggal = [int(i) for i in listTanggal]
    kabisat = (int(listTanggal[2]) % 400 == 0) or ((int(listTanggal[2]) % 100 != 0) and (int(listTanggal[2]) % 4 == 0))
    
    if int(listTanggal[1]) in [1, 3, 5, 7, 8, 10, 12]:
        return listTanggal[0] in range(1, 32, 1)
    elif listTanggal[1] == 2 and listTanggal[0] == 29:
        return kabisat
    elif listTanggal[1] in [2, 4, 6, 9, 11]:
        return listTanggal[0] in range(1, 28)
    else:
        return False
    
def helper (userRole):
    if userRole=="admin":
        print("\n========== HELP =========")
        print("register - untuk melakukan registrasi user baru")
        print("login - untuk melakukan login ke dalam sistem")
        print("tambahitem - untuk melakukan penambahan item")
        print("carirarity - untuk melakukan pencarian gadget berdasarkan rarity")
        print("caritahun - pencarian gadget berdasarkan tahun ditemukannya")
        print("hapusitem - menghapus gadget atau consumable yang pernah disimpan")
        print("ubahjumlah - menambah atau mengurangi gadget atau consumable yang pernah disimpan")
        print("riwayatpinjam - melihat riwayat peminjaman gadget")
        print("riwayatkembali - melihat riwayat pengembalian gadget")
        print("riwayatambil - melihat riwayat pengembalian consumable")
        print("save - menyimpan data ke dalam file setelah dilakukan perubahan")
        print("exit - keluar dari aplikasi\n")
        return ()
    elif userRole=="user":
        print("\n========= HELP ==========")
        print("login - untuk melakukan login ke dalam sistem")
        print("carirarity - untuk melakukan pencarian gadget berdasarkan rarity")
        print("caritahun - pencarian gadget berdasarkan tahun ditemukannya")
        print("pinjamgadget - meminjam gadget")
        print("kembalikan - mengembalikan gadget")
        print("minta - meminta consumable yang tersedia")
        print("save - menyimpan data ke dalam file setelah dilakukan perubahan")
        print("exit - keluar dari aplikasi\n")
        return ()
    else:
        print("\n========= HELP ==========")
        print("login - untuk melakukan login ke dalam sistem")
        print("exit - keluar dari aplikasi\n")   