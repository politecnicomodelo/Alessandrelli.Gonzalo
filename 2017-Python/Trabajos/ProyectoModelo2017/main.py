from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

#@app.route('/ProyectoLoL')
#def index():
    #return render_template('ProyectoLoL.html')



if __name__ == '__main__':
    app.run(debug = True, port = 5000)
