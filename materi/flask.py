from flask import Flask, redirect, render_template, request, url_for
import sqlite3 
app = Flask(__name__)
@app.route('/success/<name>', methods=['GET'] )
def success(name):
  return 'Proses data user : %s berhasil' % name
@app.route("/registeruser", methods=['POST']) 
def registeruser():
 if request.method == "POST": 
  realname = request.form['realname']
  pob = request.form['pob']  
  username = request.form['username']
  password = request.form['password']
  saveUserToDB(realname, pob, username, password)  
  return redirect(url_for('success', name = username))
def saveUserToDB(realname, pob, username, password):
 connection = sqlite3.connect("user.db")
 cursor = connection.cursor()
 cursor.execute("INSERT INTO user (realname, pob, username, password) VALUES (?, ?, ?, ?);", 
    (realname, pob, username, password))
 connection.commit()
 connection.close()

if __name__ == '__main__':
  app.run()
