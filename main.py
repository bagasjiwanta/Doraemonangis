import os 
import sys
from time import sleep 
from modules import csvParser
from modules import randomizer
from modules import access

# Files & data structure 
userFiles = os.path.join(sys.path[0], 'src/user.csv')
gadgets = os.path.join(sys.path[0], 'src/gadget.csv')
gadgetBorHis = os.path.join(sys.path[0], 'src/gadget_borrow_history.csv')
gadgetRetHis = os.path.join(sys.path[0], 'src/gadget_borrow_history.csv')
consumables = os.path.join(sys.path[0], 'src/consumable.csv')
consumablesHis = os.path.join(sys.path[0], 'src/consumable_history.csv')
# end of Files & Data Structure 

# GUI section 
# end of GUI section 

userID = ''
userStatus = ''

if __name__=="__main__":

    # ini harusnya masuk ke GUI sih tpi tolong dong dibikinin nanti GUI nya 
    # gw nggak ngide mau gimana :( 
    sleep(1)
    print("\n---------------------\nSelamat datang di kantong ajaib\n"
    "---------------------\nMasukkan command")
    command = '' 
    sleep(1)
    # 

    while True:
        command = input("[%s:%s] > "%(userStatus, userID))
        if command.lower() == "exit":
            exit
            break 

        elif command.lower() == "register":
            access.register(userFiles, userStatus)

        elif command.lower() == "login":
            userID, userStatus = access.login(userFiles)

        else:
            print("command tidak dikenali, coba lagi")
    
       