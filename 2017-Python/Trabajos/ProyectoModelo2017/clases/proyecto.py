class Proyecto (object):
    id_proyecto = None
    titulo = None
    descripcion = None
    imagenes = []


    def __init__(self , id , cursor):
        self.id_proyecto = id
        self.titulo = self.obtener_titulo(id , cursor)
        self.descripcion = self.obtener_descripcion(id, cursor)
        self.imagenes = self.obtener_imagenes(id, cursor)


    def obtener_titulo (self , id , cursor):
        cursor.execute("select entregar_titulo ("+str(id)+")")
        self.titulo = cursor.fetchall()
        return self.titulo

    def obtener_descripcion (self , id , cursor):
        cursor.execute("select entregar_descripcion ("+str(id)+")")
        self.descripcion = cursor.fetchall()
        return self.descripcion

    def obtener_imagenes (self , id , cursor):
        self.imagenes = Imagen()
        self.imagenes.__init__(id , cursor)
        return self.imagenes

    def obtener_integrantes(self, cursor , id):
        integrante = Integrante()
        integrante.__init__(cursor, id)



class Integrante (object):
    dni = None
    nombre = None
    apellido = None
    curso = None
    edad = None
    imagen = None

    def __init__(self, cursor, id):
        self.dni = self.obtener_dni(cursor, id)
        self.nombre = self.obtener_nombre(cursor, id)
        self.apellido = self.obtner_apellido(cursor, id)
        self.curso = self.obtener_curso(cursor, id)
        self.edad = self.obtener_edad(cursor, id)
        self.imagen = self.obtener_imagen(cursor, id)
        return self.nombre, self.apellido

    def obtener_nombre(self, cursor, id):
        cursor.execute("select integrante.nombre from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = ("+str(id)+")")
        self.nombre = cursor.fetchall()

    def obtener_dni(self, cursor, id):
        cursor.execute("select integrante.dni from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.dni = cursor.fetchall()

    def obtner_apellido(self, cursor, id):
        cursor.execute("select integrante.apellido from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.apellido = cursor.fetchall()

    def obtener_curso(self, cursor, id):
        cursor.execute("select integrante.curso from integrante "
                        "join integrnte_has_proyecto"
                        "on integrante.dni = integrante_has_proyecto.integrante.dni"
                        "where integrante_has_proyecto = (" + str(id) + ")")
        self.curso = cursor.fetchall()

    def obtener_edad(self, cursor, id):
        cursor.execute("select integrante.edad from integrante "
                       "join integrnte_has_proyecto"
                       "on integrante.dni = integrante_has_proyecto.integrante.dni"
                       "where integrante_has_proyecto = (" + str(id) + ")")
        self.edad = cursor.fetchall()

    def obtener_imagen(self, cursor, id):
        cursor.execute("select integrante.imagen from integrante "
                       "join integrnte_has_proyecto"
                       "on integrante.dni = integrante_has_proyecto.integrante.dni"
                       "where integrante_has_proyecto = (" + str(id) + ")")
        self.imagen = cursor.fetchall()



class Imagen (object):
    id_imagen = None
    imagen = None
    descripcion = None

    def __init__(self, id, cursor):
        self.id_imagen = self.obtener_id_imagen(id , cursor)
        self.imagen = self.obtener_imagenes(id , cursor)
        self.descripcion = self.obtener_descipcion(id , cursor)
        return self.imagen

    def obtener_imagenes (self , id , cursor):
        cursor.execute("call dar_imagenes(" + str(id) + ")")
        self.imagen = cursor.fetchall()
        return self.imagen

    def obtener_descipcion (self , id , cursor):
        cursor.execute("call descripcion_imagenes(" + str(id) + ")")
        self.descripcion = cursor.fetchall()
        return self.descripcion

    def obtener_id_imagen(self , id , cursor):
        cursor.execute("select id_imagen from imagen where proyecto_id_grupo = (" + str(id) + ")")
        self.id_imagen = cursor.fetchall()
        return self.id_imagen