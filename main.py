from cryptography.fernet import Fernet
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def render():
    return render_template("index.html")

# def print_hi(name):
#     # key = Fernet.generate_key()
#     key = load_form_file()
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



# def encrypt() #file
#     #byty pliku z przegladaki
#      #zapisuje do FILES plik ze zmienioną nazwa
#
# def decrypt(id_pliku)
#     # ma zwrocick odkodowany plik
#
# def pobierz_wszystkie_pliki():
#     pass
# #lista plikow z katalogu FILES - spr na necie


if __name__ == '__main__':
    app.run(port=7000)
