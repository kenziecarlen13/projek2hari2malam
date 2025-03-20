from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=['POST']) 
def login():
    username = request.form['username']
    password = request.form['password']
    
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()

    # Ambil password dari database berdasarkan username
    cursor.execute("SELECT password FROM user WHERE username=?;", (username,))
    row = cursor.fetchone()
    connection.close()

    # Jika username ditemukan dan password cocok, render halaman resultLogin.html
    if row and row[0] == password:
        return render_template('resultLogin.html', username=username)  
    return render_template('loginGagal.html')

if __name__ == "__main__":
    app.run(debug=True)
