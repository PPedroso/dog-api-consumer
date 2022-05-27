from dog_api import *
import os

user_input = ''

while True:
    os.system('cls')
    print('1 - Get all breeds')
    print('0 - Quit')

    user_input = input()

    if user_input == '1':
        breeds = get_all_breeds()

        for breed in breeds:
            print(breed)
    
    if user_input == '0':
        break
    
    input("Press any key to continue")    
    