# JADIKAN REFERENSI (BELUM DIIMPLEMENTASI)
# Source: Bayu Samudra (16520420) - 8 April 2021

# Module Constant
# Modul ini beris semua konstanta dinamis 
# yang digunakan pada Program ini

from os.path import join, abspath, dirname

# KAMUS
# constant MAX_ITEM : integer = 100
MAX_ARRAY_NUM = 10000

# RANDOM GENERATOR SETTINGS
# constant A_COEF : integer
A_COEF = 0x3EFB28A38257
# constant MOD_COEF : integer
MOD_COEF = 2**64-1
# constant C_COEF : integer
C_CONST = 1

# HASH SETTINGS
# constant HASH_LEN : integer
HASH_LEN = 64
# constant HASH_INIT_CONST : integer
HASH_INIT_CONST = 0x85D6E242656AAFF
# constant HASH_CONST_1 : integer
HASH_CONST_1 = 0x2443
# constant HASH_CONST_2 : integer
HASH_CONST_2 = 0x4D95
# constant HASH_ROUND : integer
HASH_ROUND = 80

# DATABASE
# constant DB_FILES_NAME : array[0..5] of string
DB_FILES_NAME = (["consumable_history.csv", 
                 "consumable.csv",
                 "gadget_borrow_history.csv",
                 "gadget_return_history.csv",
                 "gadget.csv",
                 "user.csv"], 6)

#  Module hash
"""Modul ini berisi semua fungsi yang berkaitan dengan
proses hashing string."""

# PUSTAKA
from math import log2


#from core.constant import HASH_CONST_1, HASH_CONST_2, \
        #HASH_INIT_CONST, HASH_LEN, HASH_ROUND

# KAMUS

# function intHash(str: string) -> integer
# Fungsi ini akan menerima sebuah string str lalu akan
# menghitung nilai hashnya. Hash yang dihasilkan akan
# memiliki besar HASH_LEN bit (64 bit)

# function hash(str: string) -> string
# Fungsi ini akan menerima ssebuah string str lalu akan
# menghitung nilai hasnya menggunakan fungsi intHash,
# lalu akan mengeluarkan hasil hash dalam heksadesimal
# dengan tipe data string sepanjang 16 karakter

# function padding(num: integer) -> integer
# Fungsi ini akan membuat num akan memiliki besar
# dengan kelipatan 2^HASH_LEN (dengan HASH_LEN = 64)
# dengan cara menempelkan 1 pada bit terakhir lalu 
# menambah 0 hingga jumlah bit mencapai panjang yang 
# sesuai. Jika num sudah 64 bit, maka hasil dikeluarkan

# function bitLength(num:integer) -> integer
# Fungsi ini akan menghitung panjang bit dari num

# function strToInt(str:string) -> integer
# Fungsi ini akan mengubah string menjadi bilangan
# integer

# function fungsiPengacak(num:integer) -> integer
# Fungsi ini menerima bilangan 64 bit dan fungsi ini
# akan mengacak bit dari num dan mengeluarkan bilangan 
# hasil dari pengacakan bit dari num maksimal sepanjang
# 64 bit jika tidak akan menghasilkan error den 
# mengembalikan nilai -1

def intHash(str: str) -> int:
    """Fungsi ini menerima sebuah variabel string dan
    akan menghasilkan string yang merupakan nilai hash
    dari input."""
    # KAMUS LOKAL
    # bits, result : integer

    # ALGORITMA
    bits = padding(strToInt(str))
    result = HASH_INIT_CONST

    while(bits != 0):
        currentBits = (bits % 2 ** 64)
        result = (result + fungsiPengacak(currentBits)) % (2 ** 64)
        bits //= 2 ** 64
    
    return result

def hash(str: str) -> str: #FUNGSI UTAMA
    """Fungsi ini menerima sebuah string dan akan
    menghasilkann string berupa angka heksadesimal dari
    fungsi hash (64 bit)"""
    # KAMUS LOKAL
    # hexResult : string

    # ALGORITMA
    hexResult = intToHex(intHash(str))

    if len(hexResult) < 16:
        return "0" * (16-len(hexResult)) + hexResult
    else:
        return hexResult

def padding(num: int) -> int:
    """Fungsi ini akan membuat num akan memiliki besar
    dengan kelipatan (HASH_LEN) bit"""
    # KAMUS
    #   isOneInserted : boolean {Penanda apakah bit 1
    #                      sudah dimasukan atau belum }

    # ALGORITMA
    isOneInserted = False
    while  (bitLength(num) < HASH_LEN 
            or bitLength(num) % HASH_LEN != 0):
        if(not isOneInserted):
            num = num * 2 + 1
            isOneInserted = True
        else:
            num *= 2
    
    return num

def bitLength(num : int) -> int:
    """Fungsi ini akan menghitung jumlah bit dari num."""
    # KAMUS LOKAL

    # ALGORITMA
    if(num > 0):
        return int(log2(num)) + 1
    else:
        return 0

def strToInt(str:str) -> int:
    """Fungsi strToInt akan mengubah str menjadi integer"""
    # KAMUS
    #   sum : integer { Hasil konversi }

    # ALGORITMA
    sum = 0
    for i in range(len(str)):
        sum *= 256
        sum += ord(str[i])
    
    return sum

def fungsiPengacak(num:int) -> int:
    """Fungsi pengubah akan menerima bilangan integer maksimal sepanjang
    64 bit lalu akan melakukan proses pengacakan num dan mengeluarkan
    bilangan bulat baru sepanjang 64 bit."""
    # KAMUS LOKAL
    # start_num, appendElm : integer
    # bitArray16, newBitArray : array[0..3] of integer
    # i : integer

    # ALGORITMA
    if bitLength(num) > 64:
        print("KESALAHAN! Fungsi harus menerima bilangan maksimal 64 bit")
        return (-1)
    else:
        start_num = num

        for i in range(HASH_ROUND):
            bitArray16 = [0,0,0,0]
            i = 0

            # Memecah bit
            while (start_num > 0):
                bitArray16[i] = start_num % (2 ** 16)
                start_num //= 2 ** 16
                i += 1
            
            # Menghitung Elemen awal yang baru
            appendElm = (bitArray16[0] + bitArray16[2]) % 2 ** 16
            appendElm = (appendElm + HASH_CONST_1) % 2 ** 16
            appendElm = ((bitArray16[1] + bitArray16[3]) * HASH_CONST_2) % 2 ** 16
            appendElm = (appendElm * 2) % 2 ** 16

            # Menjumlahkan dua suku yang bertetangga lalu geser
            newBitArray = [0,0,0,0]
            for i in range(3,0,-1):
                newBitArray[i] = bitArray16[i-1] + bitArray16[i]
            
            newBitArray[0] = appendElm
            bitArray16 = newBitArray

            # Mengubah kembali ke bilangan integer
            start_num = 0

            for i in range(3,-1,-1):
                start_num *= (2 ** 16)
                start_num += bitArray16[i]

            start_num %= 2 ** 64

        return start_num


def intToHex(num:int)->str:
    """Fungsi ini menerima sebuah integer num
    dan mengeluarkan hasil heksadesimal dari num"""

    # KAMUS LOKAL
    # hexNumber : array[0..15] of character
    # result : string

    # ALGORITMA
    hexNumber = "0123456789abcdef"
    result = ""

    while (num > 0):
        result += hexNumber[num % 16]
        num //= 16
    
    return result




