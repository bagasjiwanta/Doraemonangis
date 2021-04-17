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
    listTanggal = []
    if len(tanggal) == 10:
        for i in tanggal:
            part = ''
            if i != '/':
                part += i
            elif i == '/' or i == '0':
                listTanggal.append(part)
                continue
            else:
                print("Tanggal tidak sesuai format")
                return False
    else:
        print("Tanggal tidak sesuai format")
        return False 
    
    kabisat = (int(listTanggal[0]) % 400 == 0) or ((int(listTanggal[2]) % 100 != 0) and (int(listTanggal[2]) % 4 == 0))

    if int(listTanggal[1]) in ['01', '03', '05', '07', '08', '10', '12']:
        return listTanggal[0] in range(1, 32)
    elif listTanggal[1] == '02' and listTanggal[0] == '29':
        return kabisat
    elif listTanggal[1] in ['02', '04', '06', '09', '11']:
        return listTanggal[0] in range(1, 28)
    else:
        return False
