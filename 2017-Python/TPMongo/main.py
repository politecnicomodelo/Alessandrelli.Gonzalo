from flask import Flask, render_template
import csv


x=[]
y=[]
barrio=[]
capacidad=[]
nombre=[]
c=0
h=0

with open('locales-bailables.csv') as mongo:
    reader = csv.reader(mongo, delimiter=";")
    for row in reader:
        if c==0:
            c=c+1
            pass
        else:
            x.append(row[0])
            y.append(row[1])
            barrio.append(row[24])
            if row[7] == ' ':
                capacidad.append(1)
            else:
                capacidad.append(int(row[7]))
            nombre.append(row[4])





app = Flask(__name__)


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/barras')
def barras():
    chico = 0
    med = 0
    gran = 0

    for item in capacidad:
        if item < 1000:
            chico += 1

        elif (item >= 1000) and (item < 2000):
            med += 1

        else:
            gran += 1

    nombre = "Cuadro Mongo"

    return render_template('barras.html', capacidad=capacidad, nombre=nombre, gran=gran, med=med, chico=chico)

@app.route('/torta')
def torta():
    chico = 0
    med = 0
    gran = 0

    for item in capacidad:
        if item < 1000:
            chico += 1

        elif (item >= 1000) and (item < 2000):
            med += 1

        else:
            gran += 1

    return render_template('torta.html', capacidad=capacidad, gran=gran, med=med, chico=chico)

@app.route('/maps')
def maps():
   return render_template('maps.html')


if __name__ == '__main__':
   app.run(debug = True, port = 8000)

