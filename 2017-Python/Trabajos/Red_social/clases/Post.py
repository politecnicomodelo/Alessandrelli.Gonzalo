import pymysql
from datetime import date

class post (object):
    id_post = None
    fecha = None
    descripcion = None
    id_pagina = None
    id_grupo = None
    archivos_multimedia = []
    correo_electronico = None
