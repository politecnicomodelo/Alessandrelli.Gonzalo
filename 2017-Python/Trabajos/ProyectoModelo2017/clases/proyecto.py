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
        cursor = db.cursor(pymysql.cursors.DictCursor)
        self.imagenes = Imagen()
        self.imagenes.obtener_imagenes(id, db)
        return self.imagenes

    def obtener_integrantes(self, db , id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        integrante = Integrante()
        integrante.obtener_nombre(cursor, id)



class Integrante (object):
    dni = None
    nombre = None
    apellido = None
    curso = None
    edad = None
    imagen = None


    def obtener_nombre(self, db, id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select integrante.nombre from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = ("+str(id)+")")
        self.nombre = cursor.fetchall()

    def obtener_dni(self,db , id):
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
        cursor.callproc("dar_imagenes",(id,self.imagen))
        self.imagen = cursor.fetchall()
        return self.imagen

    def obtener_descipcion (self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("call descripcion_imagenes(" + str(id) + ")")
        self.descripcion = cursor.fetchall()
        return self.descripcion

    def obtener_id_imagen(self , id , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select id_imagen from imagen where proyecto_id_grupo = (" + str(id) + ")")
        self.id_imagen = cursor.fetchall()
        return self.id_imagen


