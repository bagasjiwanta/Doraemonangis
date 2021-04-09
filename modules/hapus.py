from .csvParser import openParse, writeParse, combineParse

def hapusconsum(consumID, listconsum, consumListCsv):
    index = 0
    for i in listconsum:
        if i[0] == consumID:
            caution = input("Apakah anda yakin ingin menghapus %s (Y/N)? "%(i[1]))
            if caution.lower() == 'y':
                listconsum.remove(i)
                print(listconsum)
                writeParse(combineParse(listconsum), consumListCsv)
                break
            else: 
                break 
             
    else: 
        print("\nTidak ada item dengan ID tersebut.")


def hapusgadget(gadgetID, listgadget, gadgetListCsv):
    index = 0
    for i in listgadget:
        if i[0] == gadgetID:
            caution = input("Apakah anda yakin ingin menghapus %s (Y/N)? " %(i[1]))
            if caution.lower() == 'y':
                listgadget.remove(i)
                writeParse(combineParse(listgadget), gadgetListCsv)
                break
            else: 
                break 
             
    else: 
        print("\nTidak ada item dengan ID tersebut.")
