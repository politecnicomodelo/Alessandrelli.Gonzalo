import pymysql
from clases.Usuario import Usuario
from flask import Flask, render_template , request
import hashlib
from datetime import date
from socket import *
import wmi

HTTP_STATIC="http://127.0.0.1/"
#db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
#                      db = "red_social" , autocommit = True)
#cursor = db.cursor()

#c=wmi.WMI('172.16.2.250',user='root',password='alumno')
#process_id, return_value = c.Win32_Process.Create(CommandLine="cmd.exe /c  <your command>")

app = Flask(__name__)
@app.route('/')
def index():
    lista = ["amigo1","amigo2","amigo3","amigo4","amigo5"]
    return render_template('index.html', static = HTTP_STATIC,  lista = lista)
    id = request.args.get('id')
if __name__ == '__main__':
    app.run(debug = True, port = 5000)