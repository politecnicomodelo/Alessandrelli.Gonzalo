from flask import Flask
from flask import render_template


import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" , db = "expo_modelo_2017_computacion" , autocommit = True)
c= db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "titulo"
    descripcion = "descripcion"
    espacio = " "
    imagenes = ["foto1.png", "foto2.png"]#lista de rutas de fotos del proyecto.
    return render_template('Index.html', titulo = titulo, descripcion= descripcion, imagenes= imagenes, espacio = espacio)

@app.route('/Proyecto')
def proyecto_titulo(titulo):
    return render_template('Proyecto.html', titulo = titulo)


if __name__ == '__main__':
    app.run(debug = True, port = 5000)