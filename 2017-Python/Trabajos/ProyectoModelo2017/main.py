import os.path

from flask import Flask
from flask import request
from flask import render_template
from clases.proyecto import *

import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)


app = Flask(__name__, static_url_path='/static')


def ObtenerProyecto(id, db):
    proyecto = Proyecto()
    titulo = proyecto.obtener_titulo(id, db)
    descripcion = proyecto.obtener_descripcion(id, db)
    imagenes, descripcionImagen = proyecto.obtener_imagenes(id, db)

    return titulo, descripcion, imagenes, descripcionImagen



@app.route('/')
def index():
    cursor = db.cursor()
    titulo, descripcion, imagenes, descripcionImagen = ObtenerProyecto(0, db)
    guia = "COLOCA UNA PIEZA PARA SABER MAS INFORMACION SOBRE ESE PROYECTO"
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, descripcionImagen = descripcionImagen ,guia = guia)


@app.route('/Proyecto')
def proyecto ():
    cursor = db.cursor()
    titulo, descripcion, imagenes = ObtenerProyecto(3, db)
    return render_template('Proyecto.html', titulo = titulo,  descripcion = descripcion, imagenes = imagenes)


if __name__ == '__main__':
    app.run(debug = True, port = 5000)