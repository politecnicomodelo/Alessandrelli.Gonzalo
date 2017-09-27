import pymysql


class Proyecto (object):
    id_proyecto = None
    titulo = None
    descripcion = None
    imagenes = []


    def obtener_titulo (self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select nombre from proyecto where id_grupo = ("+str(id)+")")
        self.titulo = cursor.fetchall()
        return self.titulo[0]['nombre']

    def obtener_descripcion (self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select descripcion from proyecto where id_grupo = ("+str(id)+")")
        self.descripcion = cursor.fetchall()
        return self.descripcion[0]['descripcion']

    def obtener_imagenes (self , id , db):
        self.imagenes = Imagen()
        return self.imagenes.obtener_imagenes(id, db)

    def obtener_descripcionImagen (self , id , db):
        self.descripcion = Imagen()
        return self.descripcion.obtener_descripcion(id, db)

    def obtener_integrantes(self, db, id):
        integrante = Integrante()
        return integrante.obtener_nombre(db, id)

    def obtener_curso(self, id, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select curso from proyecto where id_grupo = (" + str(id) + ")")
        self.descripcion = cursor.fetchall()
        return self.descripcion[0]['curso']


class Integrante (object):
    dni = None
    nombre = None
    apellido = None
    curso = None
    edad = None
    imagen = None


    def obtener_nombre(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.apellido from integrante join integrante_has_proyecto on integrante.dni = integrante_has_proyecto.integrante_dni where integrante_has_proyecto.proyecto_id_grupo = ("+str(id)+")")
        self.nombre = cursor.fetchall()
        if id == 3 or id == 5 or id == 1: return self.nombre[0]['apellido'], self.nombre[1]['apellido'], self.nombre[2]['apellido'], " ", " "
        elif id == 0: return self.nombre[0]['apellido'], self.nombre[1]['apellido'], self.nombre[2]['apellido'], self.nombre[3]['apellido'], self.nombre[4]['apellido']
        else: return self.nombre[0]['apellido'], self.nombre[1]['apellido'], " ", " ", " "

    def obtener_dni(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.dni from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.dni = cursor.fetchall()

    def obtner_apellido(self,db , id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.apellido from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.apellido = cursor.fetchall()

    def obtener_curso(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.curso from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.curso = cursor.fetchall()

    def obtener_edad(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.edad from integrante "
                       "join integrnte_has_proyecto"
                       "on integrante.dni = integrante_has_proyecto.integrante.dni"
                       "where integrante_has_proyecto = (" + str(id) + ")")
        self.edad = cursor.fetchall()

    def obtener_imagen(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.imagen from integrante "
                       "join integrnte_has_proyecto"
                       "on integrante.dni = integrante_has_proyecto.integrante.dni"
                       "where integrante_has_proyecto = (" + str(id) + ")")
        self.imagen = cursor.fetchall()



class Imagen (object):
    id_imagen = None
    imagen = None
    descripcion = None



    def obtener_imagenes (self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        self.imagen = None
        cursor.execute("select imagen from imagen where id_grupo = "+ str(id))
        self.imagen = cursor.fetchall()
        return self.imagen[0]['imagen']

    def obtener_descripcion (self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select descripcion_imagen from imagen where id_grupo =" + str(id) )
        self.descripcion = cursor.fetchall()
        return self.descripcion[0]['descripcion_imagen']

    def obtener_id_imagen(self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select id_imagen from imagen where proyecto_id_grupo = (" + str(id) + ")")
        self.id_imagen = cursor.fetchall()
        return self.id_imagen


