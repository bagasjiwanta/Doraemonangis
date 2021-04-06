import os 
import sys
from modules import csvParser 

userFiles = os.path.join(sys.path[0], 'src/user.csv')

if __name__=="__main__":
    command = '' 
    while command != 'exit':
        command = input()
        if command.lower() == "csvparse":
            print(csvParser.parser(userFiles))
        elif command.lower() == "exit":
            exit 