import pymysql
from clases.Usuario import Usuario
from flask import Flask, render_template , request
import hashlib
from datetime import date

HTTP_STATIC="http://127.0.0.1/"
#db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
#                      db = "red_social" , autocommit = True)
#cursor = db.cursor()






app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html', static = HTTP_STATIC)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)