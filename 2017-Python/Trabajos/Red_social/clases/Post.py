import pymysql
from datetime import date

class Post (object):
    id_post = None
    fecha = None
    descripcion = None
    id_pagina = None
    id_grupo = None
    archivos_multimedia = []
    correo_electronico = None
