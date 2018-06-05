from flask import Flask, render_template
import csv


x=[]
y=[]
capacidad=[]
nombre=[]
with open('locales.csv') as mongo:
   reader = csv.reader(mongo)
   for row in reader:
       x.append(row[0])
       y.append(row[1])
       capacidad.append(row[8])
       nombre.append(row[4])

app = Flask(__name__)


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/barras')
def barras():
   return render_template('barras.html', capacidad=capacidad, nombre=nombre)

@app.route('/maps')
def maps():
   return render_template('maps.html')


if __name__ == '__main__':
   app.run(debug = True, port = 8000)

