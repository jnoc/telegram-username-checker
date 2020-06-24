from telethon import TelegramClient, sync
from telethon import functions, types
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

id = config.get('default','api_id')
hash = config.get('default','api_hash')

if id =='UPDATE ME' or hash == 'UPDATE ME':
    print("Please read the config.ini")
    input()
    exit()
else:
    id = int(id)
    client = TelegramClient('Checker', id, hash)
    client.start()

def userLookup():

    account = str(input("Name: "))
    result = client(functions.account.CheckUsernameRequest(username=account))
    if result == True:
        print("The telegram", account, "is available")
        
    else:
        print("The telegram", account, "is not available")
        
        
def main():
        print('''
▄▄▄█████▓▓█████  ██▓    ▓█████   ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓█   ▀  ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
▒ ▓██░ ▒░▒███   ▒██░    ▒███   ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒▓█  ▄ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
  ▒██▒ ░ ░▒████▒░██████▒░▒████▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
  ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
    ░     ░ ░  ░░ ░ ▒  ░ ░ ░  ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
  ░         ░     ░ ░      ░   ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
            ░  ░    ░  ░   ░  ░      ░    ░           ░  ░       ░   
                                                                     
                            - Checker -
        
        ''')
        #Make sure to read the config.ini and README.md on github
        while True:
            userLookup()
main()