from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods = ['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods = ['POST'])
def caesar_decrypt():
        text = request.form['inputCipherText']
        key = int(request.formp['inputCipherText'])
        Caesar = CaesarCipher()
        decrypted_text = Caesar.decrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods = ['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods = ['POST'])
def vigenere_decrypt():
        text = request.form['inputCipherText']
        key = int(request.formp['inputCipherText'])
        Vigenere = VigenereCipher()
        decrypted_text = Vigenere.decrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt", methods = ['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods = ['POST'])
def railfence_decrypt():
        text = request.form['inputCipherText']
        key = int(request.formp['inputCipherText'])
        Railfence = RailFenceCipher()
        decrypted_text = Railfence.decrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)