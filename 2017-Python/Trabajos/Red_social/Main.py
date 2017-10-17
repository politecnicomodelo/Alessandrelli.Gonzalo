import pymysql
from flask import Flask, render_template , request
from clases.Usuario import Usuario
from clases.Amigo import Amigo
from clases.Grupo import Grupo
from clases.Pagina import Pagina
from clases.Post import Post
from clases.Multimedia import Multimedia
from clases.Pagina_participa import Pagina_participa
from clases.Grupo_participa import Grupo_participa
from clases.Chat import Chat
import hashlib
from datetime import date

HTTP_STATIC="http://127.0.0.1/"
db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
                      db = "red_social" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)

cursor.execute("select * from Usuario")

datos = cursor.fetchall()
lista_usuarios = []

for item in datos:
    mi_usuario = Usuario()
    mi_usuario.id_usuario = item[0]
    mi_usuario.formacion_empleo = item[1]
    mi_usuario.lugares_vividos = item[2]
    mi_usuario.informacion_basica = item[3]
    mi_usuario.acontecimientos_importantes = item[4]
    mi_usuario.nombre = item[5]
    mi_usuario.apellido = item[6]
    mi_usuario.correo_electronico = item[7]
    mi_usuario.numero_tarjeta_credito = item[8]
    mi_usuario.fecha_vencimiento_tarjeta = item[9]
    mi_usuario.codigo_seguridad_tarjeta = item[10]
    mi_usuario.fecha_nacimiento = item[11]
    mi_usuario.genero_sexual = item[12]
    mi_usuario.contrasena_hash = item[13]
    lista_usuarios.append(mi_usuario)

mi_usuario = Usuario()
mi_usuario.correo_electronico = "1"
#mi_usuario.crear_usuario("1","1","1","1","1","1","11","1",'05-05-05',"1","1","1","1" , db)
#print(str(lista_usuarios[1].id_usuario))
print (mi_usuario.agregar_amigo("4" , db) , "holaaa")
#print (mi_usuario.agregar_amigo("2" , db))


@app.route('/')
def index():
    return render_template('Index.html', static = HTTP_STATIC)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)