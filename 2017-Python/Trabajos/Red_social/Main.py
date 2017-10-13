import pymysql
from flask import Flask, render_template , request
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

HTTP_STATIC="http://127.0.0.1/"
db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "" ,
                      db = "red_social" , autocommit = True)

cursor = db.cursor()
app = Flask(__name__)


app = Flask(__name__, static_url_path='')

cursor.execute("select idUsuario , FormacionEmpleo , LugaresVividos , InformacionBasica , AcontecimientosImportantes ,"
               " Nombre , Apellido , CorreoElectronico , NumeroTargetaCredito , FechaVencimientoTargeta"
               "CodigoSeguridadTargeta , FechaNacimiento , GeneroSexual , contrasena_hash from Usuario")

mi_usuario = Usuario()
mi_usuario.


@app.route('/')
def index():
    return render_template('Index.html', static = HTTP_STATIC)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)