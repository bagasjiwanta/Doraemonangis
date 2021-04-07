import os 
import sys
from modules import csvParser, access, random

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

if __name__=="__main__":
    command = '' 
    while True:
        command = input()
        status = "admin"
        if command.lower() == "register":
            access.register(csvParser.parser(userFiles), status)

        elif command.lower() == "exit":
            exit 
        else:
            print("command tidak dikenali, coba lagi")
    else:
        print("tubes anjeng")