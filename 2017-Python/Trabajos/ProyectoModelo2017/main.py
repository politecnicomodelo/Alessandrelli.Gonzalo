
import pymysql
from flask import Flask, request, render_template, send_from_directory
from clases.proyecto import *

HTTP_STATIC="http://172.16.2.250/"
db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)


app = Flask(__name__, static_url_path='')


def ObtenerEstadisticas(id, db):
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
    guia = "Coloca una pieza para saber mas informacion sobre el proyecto"
    return render_template('Index.html', static=HTTP_STATIC,titulo = titulo, descripcion = descripcion, imagenes = imagenes, descripcionImagen = 'Descripción de la imagen' ,guia = guia)



@app.route('/Proyecto')
def proyecto (id):
    cursor = db.cursor()
    titulo, descripcion, imagenes, descripcionImagen = ObtenerProyecto(id, db)
    Estadisticas = ObtenerEstadisticas(id, db)
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, descripcionImagen = descripcionImagen ,estadisticas = estadisticas)



if __name__ == '__main__':
    app.run(debug = True, port = 5000)