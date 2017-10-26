import pymysql

from clases.Usuario import Usuario
from flask import Flask, render_template , request
import hashlib
from datetime import date

HTTP_STATIC="http://127.0.0.1/"
db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
                      db = "red_social" , autocommit = True)
cursor = db.cursor()



#asd
lista_usuarios = []

cursor.execute("select * from usuario")
datos = cursor.fetchall()

#for item in datos:
#    mi_usuario = Usuario()

    #mi_usuario.id_usuario = item["idusuario"]
    #mi_usuario.formacion_empleo = item["formacionempleo"].split(',')
    #mi_usuario.lugares_vividos = item["lugaresvividos"].split(',')
    #mi_usuario.informacion_basica = item["informacionbasica"]
    #mi_usuario.acontecimientos_importantes = item["acontecimientos_importantes"].split(',')
    #mi_usuario.nombre = item["nombre"]
    #mi_usuario.apellido = item["apelllido"]
    #mi_usuario.correo_electronico = item["correoelectronico"]
    #mi_usuario.numero_tarjeta_credito = item["numerotarjetacredito"]
    #mi_usuario.fecha_vencimiento_tarjeta = item["fechavencimientotarjeta"]
    #mi_usuario.codigo_seguridad_tarjeta = item["codigoseguridadtarjeta"]
    #mi_usuario.fecha_nacimiento = item["fechanacimiento"]
    #mi_usuario.genero_sexual = item["generosexual"]
    #mi_usuario.contrasena_hash = item["contrasena_hash"]

#   lista_usuarios.append(mi_usuario)

mi_usuario = Usuario()
#mi_usuario.correo_electronico = "juana.rojas@hotmail.com"
#mi_usuario.id_usuario = 5

formacion_empleo = "desempleado,nunca trabaje,"
lugares_vividos = "argentina,chile,"
informacion_basica = "soy una eprsona sentimental"
acontecimientos_importantes = "murio mi abuelo en 1989,naci,"
nombre = "juan"
apellido = "jordiano"
correo_electronico = "richard.joirdano@hotmail.com"
numero_tarjeta_credito = None
fecha_vencimiento_tarjeta = None
codigo_seguridad_tarjeta = None
fecha_nacimiento = '1995-03-06'
genero_sexual = "masculino"
contrasena = "Hnvpuhkh1"

mi_usuario = mi_usuario.crear_usuario(formacion_empleo , lugares_vividos , informacion_basica , acontecimientos_importantes
                         , nombre , apellido , correo_electronico , numero_tarjeta_credito
                         , fecha_vencimiento_tarjeta , codigo_seguridad_tarjeta , fecha_nacimiento , genero_sexual
                         , contrasena , db)[0]

lista_usuarios.append(mi_usuario)

print(mi_usuario.agregar_amigo(5 , db))
print(mi_usuario.lista_amigos[0].id_amigo)



#app = Flask(__name__)
#@app.route('/')
#def index():
#   return render_template('Index.html', static = HTTP_STATIC)

#if __name__ == '__main__':
#    app.run(debug = True, port = 5000)