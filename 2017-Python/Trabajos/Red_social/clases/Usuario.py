import pymysql
from .Amigo import Amigo
from .Grupo import Grupo
from .Pagina import Pagina
from .Multimedia import Multimedia
import hashlib
from datetime import date


class Usuario (object):
    id_usuario = None
    formacion_empleo = []
    lugares_vividos = []
    informacion_basica = None
    acontecimientos_importantes = []
    nombre = None
    apelllido = None
    correo_electronico = None
    numero_tarjeta_credito = None
    fecha_vencimiento_tarjeta = None
    codigo_seguridad_tarjeta = None
    fecha_nacimiento = None
    genero_sexual = None
    contrasena_hash = None
    lista_amigos = []
    lista_grupos = []
    lista_paginas = []


    def crear_usuario (self , id , formacion , residencias , informacion , acontecimientos , nomb , ap , correo , numero_tarjeta , fecha_tarjeta , codigo_tarjeta , nacimiento , genero , contra_hash , db):
        contra_hash = self.hashear_contrasena(contra_hash)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("insert into Usuario values (("+int(id)+") , ("+str(formacion)+") , ("+str(residencias)+") , ("+str(informacion)+") , ("+str(acontecimientos)+") , ("+str(nomb)+") , ("+str(ap)+") , ("+str(correo)+") , ("+str(numero_tarjeta)+") , ("+date(fecha_tarjeta)+") , ("+str(codigo_tarjeta)+") , ("+date(nacimiento)+") , ("+str(genero)+") , ("+str(contra_hash)+"))")

        self.id_usuario = id
        self.formacion_empleo = self.crear_lista(formacion)
        self.lugares_vividos = self.crear_lista(residencias)
        self.informacion_basica = informacion
        self.acontecimientos_importantes = self.crear_lista(acontecimientos)
        self.nombre = nomb
        self.apellido = ap
        self.correo_electronico = correo
        self.numero_tarjeta_credito = numero_tarjeta
        self.fecha_vencimiento_tarjeta = fecha_tarjeta
        self.codigo_seguridad_tarjeta = codigo_tarjeta
        self.fecha_nacimiento = nacimiento
        self.genero_sexual = genero
        self.contrasena_hash = contra_hash

    def hashear_contrasena (contrasena):
        contra = hashlib.md5()
        contra.update(contrasena)
        return contra

    def crear_lista (self , dato):
        datos = []
        datos = dato.split(",")
        return datos

    def loguear (self , correo , contrasena , db):
        contrasena_hash = hashlib.md5()
        contrasena_hash.update = (contrasena)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select idUsuario from Usuario where CorreoElectronico = ("+str(correo)+") and contrasena_hash "
                                                                                               "= ("+str(contrasena_hash)+")")

        datos = cursor.fetchall()
        if (str(datos [0]['idUsuario']) == "NULL"):
            return 0
        else:
            return 1

    def agregar_amigo(self , correo_amigo, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        if (cursor.execute("select CorreoElectronico from Usuario where CorreoElectronico = (" + str(
                correo_amigo) + ")") != correo_amigo):
            return 0
        elif (cursor.execute("select usuario_CorreoElectronico from usuario_has_usuario where usuario_CorreoElectronico = (" + str(
                self.correo_electronico) + ") and usuario_CorreoElectronico1 = (" + str(correo_amigo) + ")") == self.correo_electronico):
            return 0
        else:
            cursor.execute("insert into usuario_has_usuario values (NULL , (" + str(self.correo_electronico) + ") , (" + str(
                correo_amigo) + "))")
            id = cursor.execute("select idAmigo from usuario_has_usuario where usuario_CorreoElectronico = (" + str(
                self.correo_electronico) + ") and usuario_CorreoElectronico1 = (" + str(correo_amigo) + ")")
            mi_amigo = Amigo()
            mi_amigo.id_amigo = id
            mi_amigo.mi_correo = self.correo_electronico
            self.lista_amigos.append(mi_amigo)

    def eliminar_amigo(self , correo_amigo, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        if (cursor.execute("select usuario_CorreoElectronico from usuario_has_usuario where usuario_CorreoElectronico = (" + str(
                self.correo_electronico) + ") and usuario_CorreoElectronico1 = (" + str(
                correo_amigo) + ")") != self.correo_electronico):
            return 0
        else:
            for item in self.lista_amigos:
                if (item.correo_amigo == correo_amigo):
                    id = item.id_amigo
                    self.lista_amigos.remove(item)
            cursor.execute("delete from usuario_has_usuario where IdAmigo = (" + int(id) + ")")

    def crear_grupo (self , nomb , priv , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        if (cursor.execute("select Nombre from Grupo where Nombre = (" + int(nomb) + ")") != nomb):
            return 0
        else:
            mi_grupo = Grupo()
            cursor.execute("insert into grupo values (NULL , (" + bool(priv) + ") , (" + str(nomb) + ") , (" + str(self.correo_electronico) + "))")
            mi_grupo.

    def crear_pagina (self , nomb , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_pagina = Pagina()
        mi_pagina.crear_pagina(nomb, self.correo_electronico)
        return mi_pagina

    def subir_multimedia (self , archivo , creacion , album , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_multimedia = Multimedia()
        mi_multimedia.subir_multimedia(archivo , creacion , album , self.correo_electronico)
        return mi_multimedia