import os
from io import BytesIO

from cryptography.fernet import Fernet
from flask import Flask, render_template, request, Response
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


def load_form_file():
    with open("key") as key:
        return key.read()


def encrypt(file_content, file_name):
    key = load_form_file()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(file_content)
    encrypted_file_name = fernet.encrypt(bytes(file_name, 'utf-8')).decode("utf-8")
    with open(f'FILES/{encrypted_file_name}', 'wb') as dec_file:
        dec_file.write(encrypted)


def decrypt_file_content(file_id):
    key = load_form_file()
    fernet = Fernet(key)
    with open(f'FILES/{file_id}', 'rb') as file:
        original = file.read()
        return fernet.decrypt(original)


@app.route('/get_all_file')
def pobierz_wszystkie_pliki():
    return [{'name': decode_file_name(i), "id": i} for i in os.listdir("FILES")]


def decode_file_name(encoded_fiel_name) -> str:
    key = load_form_file()
    fernet = Fernet(key)
    return fernet.decrypt(encoded_fiel_name).decode("utf-8")


@app.route('/get_file/<string:id>')
def get_file(id):
    w = FileWrapper(BytesIO(decrypt_file_content(id)))
    response = Response(w, mimetype="text/plain", direct_passthrough=True)
    response.headers.set('Content-Disposition', 'attachment', filename=decode_file_name(id))
    return response


if __name__ == '__main__':
    app.run(port=7000)
