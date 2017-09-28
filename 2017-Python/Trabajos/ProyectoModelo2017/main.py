
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
    nombre = proyecto.obtener_integrantes(db, id)
    if id == 6: listaNombre = "Quinto Computacion", " ", " ", " ", " ", " ", " "
    elif id == 2 or id == 4 : listaNombre =  nombre[0]['apellido'], nombre[1]['apellido'], " ", " ", " ", " ", " "
    elif id == 1 or id == 3 or id == 5: listaNombre =  nombre[0]['apellido'], nombre[1]['apellido'], nombre[2]['apellido'], " ", " ", " ", " "
    elif id == 7: listaNombre =  nombre[0]['apellido'], nombre[1]['apellido'], nombre[2]['apellido'], nombre[3]['apellido'], " ", " ", " "
    elif id == 0 : listaNombre =  nombre[0]['apellido'], nombre[1]['apellido'], nombre[2]['apellido'], nombre[3]['apellido'], nombre[4]['apellido'], " ", " "
    elif id == 8: listaNombre = nombre[0]['apellido'], nombre[1]['apellido'], nombre[2]['apellido'], nombre[3][ 'apellido'], nombre[4]['apellido'], nombre[5]['apellido'], nombre[6]['apellido']
    return listaNombre
@app.route('/')
def index():
    return render_template('Index.html', static = HTTP_STATIC)

@app.route('/Proyecto')
def proyecto ():
    id = 4
    titulo, descripcion, imagenes, curso  = ObtenerProyecto(id, db)
    listaNombre = ObtenerNombres(id, db)
    print (imagenes)
    return render_template('Proyecto.html', static = HTTP_STATIC, curso = curso, titulo = titulo, descripcion = descripcion, imagenes = imagenes, listaNombre = listaNombre)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)