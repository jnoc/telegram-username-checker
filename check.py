from telethon import TelegramClient, sync
from telethon import functions, types
from telethon import errors
import configparser
import time
import os


config = configparser.ConfigParser()
config.read('config.ini')

id = config.get('default','api_id')
hash = config.get('default','api_hash')

if id =='UPDATE ME' or hash == 'UPDATE ME':
    print("Please read the config.ini and README.md")
    input()
    exit()
else:
    id = int(id)
    client = TelegramClient('Checker', id, hash)
    client.start()
        
def userLookup(account):
    try: 
        result = client(functions.account.CheckUsernameRequest(username=account))
        if result == True:
            print("The telegram", account, "is available")
            
        else:
            print("The telegram", account, "is not available")
    except errors.FloodWaitError as e:
        print("Hit the rate limit, waiting", e.seconds, "seconds")
        time.sleep(e.seconds)
        
def getWords():
    words = []
    path = os.path.join("word_lists", config.get('default','wordList'))
    if path is not None:
        file = open(path, 'r', encoding='utf-8-sig')
        words = file.read().split('\n')
        file.close()
    else:
        print("Word list not found.")
    
    for i in range(len(words)):
        name = words[i]
        userLookup(name)
    print("All done")
    input("Press enter to exit...")
        
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
                                                                     
                        - Username Checker -
        Make sure to read the config.ini and README.md on github
    bulk checking may result in false positives and longer wait times
        ''')
        print("1 = Enter username manually\n2 = Read a list of usernames from the word_lists folder")
        set = ["1", "2"]
        option = input("Select your option: ")
        while True:
            if str(option) in set:
                if option == set[0]:
                    name = input("Enter a username: ")
                    userLookup(name)
                else:
                    getWords()
                    break
            else:
                option = input("1 or 2 ... Please!: ")
main()