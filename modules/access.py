# modul ini digunakan untuk melakukan login dan register

from .parser import openParse, appendParse
from .others import randomInt 

def register(userListCsv, acc):
    print()
    if acc.lower() == "admin":
 
        while True:
            nama = input("Masukkan nama: ").strip()
            found = False 
            while not found:
                username = input("Masukkan username: ").strip()
                for x in openParse(userListCsv)[1:]:
                    if x[1] == username:
                        print("\n[ERROR]\nUsername tidak tersedia atau telah digunakan. Mohon masukkan username lain.\n")
                        break
                else:
                    found = True 
    
            password = input("Masukkan password: ")
            alamat = input("Masukkan alamat: ").strip()
            if (';' in nama) or (';' in password) or (';' in alamat) or (';' in username):
                print("\n[ERROR]\nNama, password, alamat, dan username tidak boleh mengandung karakter ;\n"
                "Silahkan masukkan kembali")
                continue

            found = False 
            while not found:
                userId = randomInt(digit=6)
                for x in openParse(userListCsv):
                    if x[0] == userId:
                        break
                else:
                    found = True 
            
            newUser = ';'.join([userId, username, nama, alamat, password, "user"])
            try:
                appendParse(newUser, userListCsv)
                break
            except UnicodeEncodeError:
                print("\n[ERROR]\nNama/password/username/alamat anda mengandung karakter yang tidak dikenal")
                choice = input("Apakah anda ingin registrasi ulang ? [y/n]\n> ").lower().strip()
                if choice == 'n':
                    return '' 
                elif choice == 'y':
                    continue
                else:
                    print("Pilihan tidak dikenali, kembali ke menu awal . . .")
                    return '' 

        print(f"\nUser {username} telah berhasil register ke dalam Kantong Ajaib.\n")
        return username
        
    else:
        print("\n[ERROR]\nAnda tidak memiliki akses untuk melakukan registrasi\nSilakan login sebagai admin\n")
        return ''


def login(userListCsv, oldId, oldUserName, oldRole):
    found = True 
    while found:
        username = input("\nMasukkan username: ").strip()
        password = input("Masukkan password: ")
            
        for i in openParse(userListCsv):
            if i[1] == username and i[4] == password:
                print("\nHalo %s! Selamat datang di Kantong Ajaib. \n" %i[2])
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
