import pymysql
from flask import Flask, render_template
from clases.Usuario import Usuario
from clases.Amigo import Amigo
from clases.Grupo import Grupo
from clases.Pagina import Pagina
from clases.Post import Post
from clases.Multimedia import Multimedia
from clases.Pagina_participa import Pagina_participa
from clases.Grupo_participa import Grupo_participa
from clases.Chat import Chat
import hashlib
from datetime import date

HTTP_STATIC="http://172.16.2.250/"
db = pymysql.connect (host = '172.16.2.250' , user = "root" , password = "alumno" ,
                      db = "expo_modelo_2017_computacion" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)


app = Flask(__name__, static_url_path='')



@app.route('/')
def index():
    return render_template('Index.html', static = HTTP_STATIC)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)