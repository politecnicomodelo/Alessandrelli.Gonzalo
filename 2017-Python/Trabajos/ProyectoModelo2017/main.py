from flask import Flask
from flask import render_template
from clases.proyecto import *


import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()

app = Flask(__name__)
proyecto = Proyecto()


@app.route('/')
def index(cursor):

    guia = "COLOCA UNA PIEZA PARA SABER MAS INFORMACION SOBRE ESE PROYECTO"
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, guia = guia)


@app.route('/Proyecto')
def proyecto (titulo, descripcion, imagenes, estadisticas):
    return render_template('Proyecto.html', titulo = titulo,  descripcion = descripcion, imagenes = imagenes, estadisticas = estadisticas)


if __name__ == '__main__':
    app.run(debug = True, port = 5000)