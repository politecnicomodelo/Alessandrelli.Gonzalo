from flask import Flask
from flask import render_template


import pymysql

db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" , db = "expo_modelo_2017_computacion" , autocommit = True)
c= db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Pantalla Principal"
    descripcion = "ESTA DESCRIPCION ESTA RE LOCA"
    imagenes = ["FOTOS.PNG", "FOTOS.PNG"]#lista de rutas de fotos del proyecto
    guia = "COLOCA UNA PIEZA PARA SABER MAS INFORMACION SOBRE ESE PROYECTO"
    return render_template('Index.html', titulo = titulo, descripcion = descripcion, imagenes = imagenes, guia = guia)

@app.route('/Proyecto')
def proyecto (titulo, descripcion, imagenes, estadisticas):
    return render_template('Proyecto.html', titulo = titulo,  descripcion = descripcion, imagenes = imagenes, estadisticas = estadisticas)


def seleccionarProyecto(codigo):
    titulo = c.execute("select entregar_titulo(codigo)")
    descripcion = c.execute("select entregar_descripcion(codigo)")
    imagenes = c.execute("select dar_imagenes(codigo)")
    imagenes = imagenes.split("º")
    estadisticas = ""
    proyecto(titulo, descripcion, imagenes, estadisticas)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)