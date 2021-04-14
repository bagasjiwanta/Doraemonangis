from .csvParser import openParse, appendParse
from .randomizer import randomInt 

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


def login(userListCsv):
    found = False 
    while not found:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ")
        for i in openParse(userListCsv):
            if i[1] == username and i[4] == password:
                print("Login sukses, selamat datang %s\n" %username)
                found = True 
                status = i[5]
                IDnum = i[0]
                return username, status, IDnum
                break 

        else:  # Jika tidak ditemukan username & password yang benar
            command = ''
            print("Username atau password salah, ulangi login? [y/n]")
            while command.lower() != 'y':
                command = input("> ")
                if command.lower() == 'n':
                    found = True 
                    return '','','' 
                elif command.lower() != 'y':
                    print("command tidak dikenali, ulangi login? [y/n]")               

def save():
    
    while True:
        folderName = input("Masukkan nama folder untuk save: ").lower().strip()
        for i in folderName:
            if not i.isalnum():
                print("input folder tidak valid")
                break
        else:
            break
    
    