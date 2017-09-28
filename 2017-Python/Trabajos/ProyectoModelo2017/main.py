
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
    curso = proyecto.obtener_curso(id, db)
    return titulo, descripcion, imagenes, curso

def ObtenerNombres(id, db):
    proyecto = Proyecto()
    nombres, nombre1, nombre2, nombre3, nombre4, nombre5, nombre6 = proyecto.obtener_integrantes(db, id)
    listaNombre = nombres, nombre1, nombre2, nombre3, nombre4, nombre5, nombre6
    return listaNombre
@app.route('/')
def index():
    return render_template('Index.html', static = HTTP_STATIC)

@app.route('/Proyecto')
def proyecto ():
    id = 8
    titulo, descripcion, imagenes, descripcionImagen, curso  = ObtenerProyecto(id, db)
    listaNombre = obtenerNombres(id, db)
    return render_template('Proyecto.html', static = HTTP_STATIC, curso = curso, titulo = titulo, descripcion = descripcion, imagenes = imagenes, listaNombre = listaNombre)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)