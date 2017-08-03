from flask import Flask
from flask import render_template
from clases.proyecto import *


import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)

def eliminarCosas (titulo, descripcion, imagenes):
    pass

def ObtenerProyecto(id, db):
    proyecto = Proyecto()
    titulo = proyecto.obtener_titulo(id, db)
    descripcion = proyecto.obtener_descripcion(id, db)
    imagenes = proyecto.obtener_imagenes(id, db)
    return titulo, descripcion, imagenes



@app.route('/')
def index():
    cursor = db.cursor()
    titulo, descripcion, imagenes = ObtenerProyecto(0, db)
    #titulo, descripcion, imagenes = eliminarCosas(titulo, descripcion, imagenes)
    guia = "COLOCA UNA PIEZA PARA SABER MAS INFORMACION SOBRE ESE PROYECTO"
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, guia = guia)



@app.route('/Proyecto')
def proyecto ():
    cursor = db.cursor()
    titulo, descripcion, imagenes = ObtenerProyecto(2, db)
    return render_template('Proyecto.html', titulo = titulo,  descripcion = descripcion, imagenes = imagenes)



if __name__ == '__main__':
    app.run(debug = True, port = 5000)