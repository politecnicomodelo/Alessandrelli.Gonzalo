from flask import Flask
from flask import render_template
from .clases.proyecto import *


import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)



def ObtenerProyecto(id, cursor):
    proyecto = Proyecto()
    titulo = proyecto.obtener_titulo(id, cursor)
    descripcion = proyecto.obtener_descripcion(id, cursor)
    imagenes = proyecto.obtener_imagenes(id, cursor)
    imagenes = imagenes.split(',')
    return titulo, descripcion, imagenes



@app.route('/')
def index():
    cursor = db.cursor()
    titulo, descripcion, imagenes = ObtenerProyecto(1, cursor)
    guia = "COLOCA UNA PIEZA PARA SABER MAS INFORMACION SOBRE ESE PROYECTO"
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, guia = guia)



@app.route('/Proyecto')
def proyecto (cursor):
    titulo, descripcion, imagenes = ObtenerProyecto(2, cursor)
    return render_template('Proyecto.html', titulo = titulo,  descripcion = descripcion, imagenes = imagenes)



if __name__ == '__main__':
    app.run(debug = True, port = 5000)