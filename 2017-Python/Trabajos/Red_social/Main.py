import pymysql
from clases.Usuario import Usuario
from clases.Post import Post
from flask import Flask, render_template , request
import hashlib
from datetime import date
from socket import *
#import wmi


HTTP_STATIC="http://127.0.0.1:5000/"
#db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
#                      db = "red_social" , autocommit = True)
#cursor = db.cursor()

#c=wmi.WMI('172.16.2.250',user='root',password='alumno')
#process_id, return_value = c.Win32_Process.Create(CommandLine="cmd.exe /c  <your command>")







app = Flask(__name__ , static_url_path='/static')
@app.route('/')
def index():
    lista_amigos = ["amigo1", "amigo2", "amigo3", "amigo4", "amigo5"]
    lista_grupos = ["caca", "grupo cool"]
    lista_paginas = ["pis", "pagina cool"]
    imagen = "nene.jpg"
    lista_comentarios = ["gonzi loco: QUE BUENA FOTO" , "juana manuela: wow!!"]
    me_gusta = 0
    no_me_gusta = 60
    lol = 10
    wow = 2
    sad = 0
    beautiful = 0
    anger = 40
    mi_post = Post()
    mi_post.imagen = imagen
    mi_post.lista_comentarios = lista_comentarios
    mi_post.me_gusta = me_gusta
    mi_post.no_me_gusta = no_me_gusta
    mi_post.lol = lol
    mi_post.sad = sad
    mi_post.wow = wow
    mi_post.beautiful = beautiful
    mi_post.anger = anger
    lista_post = []
    lista_post.append(mi_post)
    lista_post.append(mi_post)

    return render_template('index.html', static = HTTP_STATIC,  lista_amigos = lista_amigos
                           , lista_grupos = lista_grupos , lista_paginas = lista_paginas , lista_post = lista_post)
    id = request.args.get('id')
if __name__ == '__main__':
    app.run(debug = True, port = 5000)