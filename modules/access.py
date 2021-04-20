# modul ini digunakan untuk melakukan login dan register

from .parser import openParse, appendParse
from .others import randomInt 

def register(userListCsv, acc):
    print()
    if acc.lower() == "admin":
        
        nama = input("Masukkan nama: ").strip()
        found = False 
        while not found:
            username = input("Masukkan username: ").strip()
            for x in openParse(userListCsv)[1:]:
                if x[1] == username:
                    print("username tidak tersedia, silahkan coba lagi")
                    break
            else:
                found = True 
 
        password = input("Masukkan password: ")
        alamat = input("Masukkan alamat: ").strip()
        
        found = False 
        while not found:
            userId = randomInt(digit=6)
            for x in openParse(userListCsv):
                if x[0] == userId:
                    break
            else:
                found = True 

        newUser = ';'.join([userId, username, nama, alamat, password, "user"])
        appendParse(newUser, userListCsv)
        print("User baru telah ditambahkan")
        return username
        
    else:
        print("Anda tidak memiliki akses untuk melakukan registrasi\nSilahkan login sebagai admin")
        return ''


def login(userListCsv, oldId, oldUserName, oldRole):
    found = True 
    while found:
        username = input("\nMasukkan username: ").strip()
        password = input("Masukkan password: ")
        for i in openParse(userListCsv):
            if i[1] == username and i[4] == password:
                print("\nLogin sukses, selamat datang %s\n" %username)
                found = False
                status = i[5]
                IDnum = i[0]
                return username, status, IDnum
                break 

        else:  # Jika tidak ditemukan username & password yang benar
            command = ''
            print("\nUsername atau password salah, ulangi login? [y/n]")
            while command.lower() != 'y':
                command = input("> ")
                if command.lower() == 'n':
                    found = False 
                    return oldUserName, oldRole, oldId
                elif command.lower() != 'y':
                    print("\nCommand tidak dikenali, ulangi login? [y/n]")               
