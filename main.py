from socket import SocketIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from dog_api import *
import os



app = Flask(__name__)
app.config['SECRET'] = 'secret123'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/images_by_breed')
def images_by_breed():
    breed = request.args.get('breed')
        
    dog_images = get_images_by_breed(breed)

    return render_template('/index.html', data = {'dog_images' : dog_images })

@app.route('/all_breeds')
def all_breeds():
    breeds = get_all_breeds()
    return render_template('/index.html', data = {'breeds' : breeds})

@app.route('/')
def index():
    return render_template('/index.html', data = {})


if __name__ == "__main__":
    socketio.run(app, host="localhost")

user_input = ''

# while True:
#     os.system('cls')
#     print('1 - Get all breeds')
#     print('2 - Get images by breed')
#     print('3 - Get random dog image')
#     print('0 - Quit')

#     user_input = input()

#     if user_input == '1':
#         breeds = get_all_breeds()

#         for breed in breeds:
#             print(breed, end = ' ')
#         print()
    
#     if user_input == '2':
#         breed = input("Iput the breed to print\n")
        
#         dog_images = get_images_by_breed(breed)

#         for image in dog_images:
#             print(image)

#     if user_input == '3':
#         random_image = get_random_image()
#         print(random_image)

#     if user_input == '0':
#         break
    
#     input("Press any key to continue")    
    