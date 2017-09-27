
import pymysql
from flask import Flask, render_template
from clases.proyecto import *

HTTP_STATIC="http://172.16.2.250/"
db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)


app = Flask(__name__, static_url_path='')


def ObtenerProyecto(id, db):
    proyecto = Proyecto()
    titulo = proyecto.obtener_titulo(id, db)
    descripcion = proyecto.obtener_descripcion(id, db)
    imagenes = proyecto.obtener_imagenes(id, db)
    descripcionImagen = proyecto.obtener_descripcionImagen(id, db)
    nombres, nombre1, nombre2, nombre3, nombre4 = proyecto.obtener_integrantes(db, id)
    curso = proyecto.obtener_curso(id, db)
    return titulo, descripcion, imagenes, descripcionImagen, nombres, nombre1, nombre2, nombre3, nombre4, curso


@app.route('/')
def index():
    titulo, descripcion, imagenes, descripcionImagen, nombres, nombre1, nombre2, nombre3, nombre4, curso = ObtenerProyecto(0, db)
    guia = "Coloca una pieza para saber mas informacion sobre el proyecto"
    return render_template('Index.html', static = HTTP_STATIC, titulo = titulo, descripcion = descripcion, imagenes = imagenes, descripcionImagen = descripcionImagen ,guia = guia)

@app.route('/Proyecto')
def proyecto ():
    id = 1
    titulo, descripcion, imagenes, descripcionImagen, nombres, nombre1, nombre2, nombre3, nombre4, curso  = ObtenerProyecto(id, db)
    return render_template('Proyecto.html', static = HTTP_STATIC, curso = curso, titulo = titulo, descripcion = descripcion, imagenes = imagenes, nombres = nombres, nombre1 = nombre1, nombre2 = nombre2, nombre3 = nombre3, nombre4 = nombre4,id = id)


if __name__ == '__main__':
    app.run(debug = True, port = 5000)