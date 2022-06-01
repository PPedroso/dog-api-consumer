from dog_api import *
import os

user_input = ''

while True:
    os.system('cls')
    print('1 - Get all breeds')
    print('2 - Get images by breed')
    print('3 - Get random dog image')
    print('0 - Quit')

    user_input = input()

    if user_input == '1':
        breeds = get_all_breeds()

        for breed in breeds:
            print(breed, end = ' ')
        print()
    
    if user_input == '2':
        breed = input("Iput the breed to print\n")
        
        dog_images = get_images_by_breed(breed)

        for image in dog_images:
            print(image)

    if user_input == '3':
        random_image = get_random_image()
        print(random_image)

    if user_input == '0':
        break
    
    input("Press any key to continue")    
    