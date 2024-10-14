from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
from HomomorphicEncryption import encrypt_data, decrypt_data
from FileOperations import read_file_to_data, write_encrypted_file, write_decrypted_file

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','py','js','exe','html'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return "Nessun file caricato", 400
    file = request.files['file']

    
    if file.filename == '':
        return "Nessun file selezionato", 400

    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Ottieni la chiave dall'input dell'utente
        encryption_key = request.form.get('encryption_key')

        # Operazione scelta (cifratura o decifratura)
        operation = request.form.get('operation')

        if operation == 'encrypt':
        
            file_data = read_file_to_data(file_path)
            encrypted_data, _ = encrypt_data(file_data)  # La chiave è interna alla libreria
            encrypted_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encrypted_' + filename)
            write_encrypted_file(encrypted_file_path, encrypted_data)
            return send_file(encrypted_file_path, as_attachment=True)

        elif operation == 'decrypt':
        
            file_data = read_file_to_data(file_path)
            decrypted_data = decrypt_data(file_data, encryption_key)  # Usa la chiave dell'utente
            decrypted_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'decrypted_' + filename)
            write_decrypted_file(decrypted_file_path, decrypted_data)
            return send_file(decrypted_file_path, as_attachment=True)

    return "Errore durante l'upload o l'elaborazione del file", 400

if __name__ == '__main__':
    app.run(debug=True)
