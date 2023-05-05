import os
import random
from io import BytesIO
from typing import BinaryIO

from cryptography.fernet import Fernet
from flask import Flask, render_template, request, send_file, send_from_directory, Response
from pip._internal.commands import download
from werkzeug.wsgi import FileWrapper

app = Flask(__name__)


@app.route('/')
def render():
    return render_template("index.html")


@app.route('/send_file', methods=['POST'])
def file():
    name = request.files['file'].filename
    encrypt(request.files['file'].read(), name)
    return ''


# def print_hi(name):
#     # key = Fernet.generate_key()
# def genereate_and_save_key():
#     mean_key = str(Fernet.generate_key())
#     open("key", "w").close()
#     with open("key", "w") as key:
#         key.write(mean_key)

def load_form_file():
    with open("key") as key:
        return key.read()


# key = load_form_file()
# zmienna = Fernet(key)
#
# print(key)
#     print(f'zapisz jednorazowy klucz, inaczej odszyfrowanie pliku nie bedzie mozliwe: {key}')
#     fernet = Fernet(key)
#     encrypted = fernet.encrypt(b'dupa blada lukasz marzeczna to mozeby byc dowolny testkst z pliku dupa blada')
#     # with open('FILES/nba', 'wb') as dec_file:
#     #     dec_file.write(encrypted)
#     print(encrypted)
#     key2 = Fernet.generate_key()
#     fernet2 = Fernet(key2)
#     decrypted = fernet2.decrypt(encrypted)
#     print(decrypted)
# with open('nba.csv', 'rb') as file:
#     original = file.read()
#     encrypted = fernet.encrypt(original)


def encrypt(file_content, file_name):
    key = load_form_file()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(file_content)
    with open(f'FILES/{file_name}', 'wb') as dec_file:
        dec_file.write(encrypted)


#     #byty pliku z przegladaki
#      #zapisuje do FILES plik ze zmienioną nazwa
#
def decrypt(file_id):
    key = load_form_file()
    fernet = Fernet(key)
    with open(f'FILES/{file_id}', 'rb') as file:
        original = file.read()
        return fernet.decrypt(original)


#     # ma zwrocick odkodowany plik
#
@app.route('/get_all_file')
def pobierz_wszystkie_pliki():
    b = [random.randint(1, 50000) for x in range(8)]
    bb = "".join(str(x) for x in b)
    return [{'name': i, "id": bb} for i in os.listdir("FILES")]


def decode_file_name(id):
    return id


@app.route('/get_file/<string:id>')
def get_file(id):
    b = decrypt(id)
    bb = BytesIO(b)
    w = FileWrapper(bb)
    return Response(w, mimetype="text/plain", direct_passthrough=True)
    #return send_from_directory(b,mimetype='application', as_attachment=True, download_name=decode_file_name(id))


if __name__ == '__main__':
    app.run(port=7000)
