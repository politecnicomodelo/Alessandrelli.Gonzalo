import pymysql
from .Amigo import Amigo
from .Grupo import Grupo
from .Pagina import Pagina
from .Post import Post
from .Multimedia import Multimedia
from .Pagina_participa import Pagina_participa
from .Grupo_participa import Grupo_participa
from .Chat import Chat
import hashlib
from datetime import date
                                                    #ARREGLAR HASHEAR CONTRASEÑA

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
    lista_multimedia = []
    lista_posts = []
    lista_conversaciones = []


    def crear_usuario (self , formacion_empleo , lugares_vividos , informacion_basica
                       , acontecimientos_importantes , nombre , apellido , correo_electronico , numero_tarjeta_credito
                       , fecha_vencimiento_tarjeta , codigo_seguridad_tarjeta , fecha_nacimiento , genero_sexual
                       , contrasena_hash , db):

        cursor = db.cursor(pymysql.cursors.DictCursor)
        contrasena_hash = self.hashear_contrasena(contrasena_hash)
        cursor.execute("insert into Usuario values (NULL , ("+str(formacion_empleo)+") , ("+str(lugares_vividos)+") "
                       ", ("+str(informacion_basica)+") , ("+str(acontecimientos_importantes)+") , ("+str(nombre)+") "
                       ", ("+str(apellido)+") , ("+str(correo_electronico)+") , ("+str(numero_tarjeta_credito)+")"
                       ", ("+str(fecha_vencimiento_tarjeta)+") , ("+str(codigo_seguridad_tarjeta)+") , ("+str(fecha_nacimiento)+")"
                       " , ("+str(genero_sexual)+") , ("+str(contrasena_hash)+"))")


        self.formacion_empleo = self.crear_lista(formacion_empleo)
        self.lugares_vividos = self.crear_lista(lugares_vividos)
        self.informacion_basica = informacion_basica
        self.acontecimientos_importantes = self.crear_lista(acontecimientos_importantes)
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.numero_tarjeta_credito = numero_tarjeta_credito
        self.fecha_vencimiento_tarjeta = fecha_vencimiento_tarjeta
        self.codigo_seguridad_tarjeta = codigo_seguridad_tarjeta
        self.fecha_nacimiento = fecha_nacimiento
        self.genero_sexual = genero_sexual
        self.contrasena_hash = contrasena_hash

    def hashear_contrasena (self , contrasena):
        #contra = hashlib.sha256()
        #contra.update(contrasena)
        #contra.digest()
        #return contra
        return contrasena

    def crear_lista (self , dato):
        datos = []
        datos = dato.split(",")
        return datos

    def loguear (self , correo , contrasena , db):
        contrasena_hash = self.hashear_contrasena(contrasena)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select CorreoElectronico from Usuario")
        datos = cursor.fetchall()

        for item in datos:
            if item["CorreoElectronico"] == correo:
                cursor.execute("select contrasena_hash from Usuario where CorreoElectronico = ("+str(correo)+")")
                datos = cursor.fetchall()
                if datos[0]["contrasena_hash"] == self.hashear_contrasena(contrasena):
                    return 1
                else:
                    return 0

    def agregar_amigo(self , correo_amigo, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select CorreoElectronico from Usuario")
        correo = cursor.fetchall()
        for item in correo:
            if item["CorreoElectronico"] == correo_amigo:
                cursor.execute("select * from usuario_has_usuario")
                datos = cursor.fetchall()
                for item in datos:
                    if ((item["usuario_CorreoElectronico"] == self.correo_electronico) and (item["usuario_CorreoElectronico1"] == correo_amigo)) or ((item["usuario_CorreoElectronico"] == correo_amigo) and (item["usuario_CorreoElectronico1"] == self.correo_electronico)):
                            return 0
                cursor.execute("insert into usuario_has_usuario values (NULL , (" + str(self.correo_electronico) + ") , (" + str(
                    correo_amigo) + "))")
                cursor.execute("select idAmigo from usuario_has_usuario where usuario_CorreoElectronico = (" + str(
                    self.correo_electronico) + ") and usuario_CorreoElectronico1 = (" + str(correo_amigo) + ")")
                id = cursor.fetchall()
                id = id[0]["idAmigo"]
                mi_amigo = Amigo()
                mi_amigo.id_amigo = id
                mi_amigo.mi_correo = self.correo_electronico
                mi_amigo.correo_amigo = correo_amigo
                self.lista_amigos.append(mi_amigo)
                return 1
        return 0

    def eliminar_amigo(self , correo_amigo , lista_amigos , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from usuario_has_usuario")
        datos = cursor.fetchall()
        for item in datos:
            if item["usuario_CorreoElectronico"] == self.correo_electronico:
                if item["usuario_CorreoElectronico1"] == correo_amigo:
                    for item in lista_amigos:
                        if ((item.mi_correo == self.correo_electronico) and (item.correo_amigo == correo_amigo)) or ((item.mi_correo == correo_amigo) and (item.correo_amigo == self.correo_electronico)):
                            cursor.execute("delete from usuario_has_usuario where ")

    def crear_grupo (self , nomb , priv , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select Nombre from Grupo where Nombre = (" + str(nomb) + ")")
        mi_nombre = cursor.fetchall()
        mi_nombre = mi_nombre[0]["Nombre"]
        if (mi_nombre == nomb):
            return 0
        else:
            mi_grupo = Grupo()
            cursor.execute("insert into grupo values (NULL , (" + bool(priv) + ") , (" + str(nomb) + ") , (" + str(self.correo_electronico) + "))")
            cursor.exeute("select IdGrupo from grupo where Nombre = (" + str(nomb) + ")")
            id = cursor.fetchall()
            id = id[0]["IdGrupo"]
            mi_grupo.id_grupo = id
            mi_grupo.privado = priv
            mi_grupo.nombre = nomb
            mi_grupo.correo_admin = self.correo_electronico
            self.lista_grupos.append(mi_grupo)
            return 1

    def crear_pagina (self , nomb , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_pagina = Pagina()
        cursor.execute("insert into Pagina values (NULL , (" + str(nomb) + ") , (" + str(self.correo_electronico) + "))")
        cursor.execute("select IdPagina from Pagina where usuario_CorreoElectronico = "
                       "(" + str(self.correo_electronico) + ") order by DESC")
        id = cursor.fetchall()
        id = id[0]["IdPagina"]
        mi_pagina.id_pagina = id
        mi_pagina.nombre = nomb
        mi_pagina.correo_admin = self.correo_electronico
        self.lista_paginas.append(mi_pagina)
        return 1

    def subir_multimedia (self , archivo , creacion , album , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_multimedia = Multimedia()
        #terminar
        cursor.execute("insert into Multimedia values (NULL , )")
        return 1

    def crear_post (self , fecha  , descripcion , id_pagina , id_grupo , id_archivos , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_post = Post()
        cursor.execute("insert into Post values (NULL , (" + date(fecha) + ") , (" + str(descripcion) + ") ,"
                       " (" + int(id_pagina) + ") , (" + str(self.correo_electronico) + ") , (" + str(id_grupo) + "))")
        cursor.execute("select idPost from post where usuario_CorreoElectronico = (" + str(self.correo_electronico) + ")"
                       "order by DESC")
        id = cursor.fetchall()
        id = id[0]["idPost"]

        for item in id_archivos:
            cursor.execute("insert into post_has_multimedia values ((" + int(id) + ") , (" + int(item) + "))")

        mi_post.id_post = id
        mi_post.fecha = fecha
        mi_post.descripcion = descripcion
        mi_post.id_pagina = id_pagina
        mi_post.id_grupo = id_grupo
        mi_post.archivos_multimedia = id_archivos
        self.lista_posts.append(mi_post)
        return 1

    def mandar_mensaje (self , id_amigo , mensaje , fecha , emisor , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_chat = Chat()
        cursor.execute("insert into Chat values(NULL , (" + str(mensaje) + ") , (" + str(id_amigo) + ") , "
                       "(" + date(fecha) + ") , (" + bool(emisor) + "))")
        cursor.execute("select idChat from Chat where usuario_has_usuario_IdAmigo = (" + int(id_amigo) + ")")
        id = cursor.fetchall()
        id = id[0]["idChat"]

        mi_chat.id_chat = id
        mi_chat.mensaje = mensaje
        mi_chat.id_amigo = id_amigo
        mi_chat.fecha = fecha
        mi_chat.emisor = emisor
        for item in self.lista_paginas:
            if (item.id_amigo == id_amigo):
                item.append(mi_chat)
        return 1

    def suscribir_pagina (self , id_pagina , admin , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_pagina = Pagina_participa()
        cursor.execute("insert into paginaparticipa values (NULL , (" + int(id_pagina) + ") , (" + bool(admin) + ")"
                       " , (" + str(self.correo_electronico) + "))")
        cursor.execute("select idPaginasParticipa from paginaparticipa where usuario_CorreoElectronico = "
                       "(" + str(self.correo_electronico) + ") order by desc")
        id = cursor.fetchall()
        id = id[0]["idPaginasParticipa"]
        mi_pagina.id_pagina_participa = id
        mi_pagina.id_pagina = id_pagina
        mi_pagina.administrador = admin
        mi_pagina.correo_electronico = self.correo_electronico
        self.lista_paginas.append(mi_pagina)

    def suscribir_grupo (self , admin , nombre , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_grupo = Grupo_participa()
        cursor.execute("insert into grupoparticipa values (NULL , (" + bool(admin) + ") , "
                       "(" + str(self.correo_electronico) + ") , (" + str(nombre) + "))")
        cursor.execute("select idGruposParticipa from grupoparticipa where usuario_CorreoElectronico = "
                       "(" + str(self.correo_electronico) + ") order by desc")
        id = cursor.fetchall()
        id = id[0]["idGruposParticipa"]
        mi_grupo.id_grupo_participa = id
        mi_grupo.administrador = admin
        mi_grupo.nombre_grupo = nombre
        mi_grupo.correo_electronico = self.correo_electronico
        self.lista_grupos.append(mi_grupo)


