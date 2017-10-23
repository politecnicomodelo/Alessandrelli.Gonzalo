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


    def crear_usuario (self , formacion_empleo , lugares_vividos , informacion_basica
                       , acontecimientos_importantes , nombre , apellido , correo_electronico , numero_tarjeta_credito
                       , fecha_vencimiento_tarjeta , codigo_seguridad_tarjeta , fecha_nacimiento , genero_sexual
                       , contrasena_hash , db):

        cursor = db.cursor(pymysql.cursors.DictCursor)
        contrasena_hash = self.hashear_contrasena(contrasena_hash)
        cursor.execute("insert into Usuario values (NULL , '"+str(formacion_empleo)+"' , '"+str(lugares_vividos)+"' "
                       ", '"+str(informacion_basica)+"' , '"+str(acontecimientos_importantes)+"' , '"+str(nombre)+"' "
                       ", '"+str(apellido)+"' , '"+str(correo_electronico)+"' , '"+str(numero_tarjeta_credito)+"'"
                       ", '"+str(fecha_vencimiento_tarjeta)+"' , '"+str(codigo_seguridad_tarjeta)+"' , '"+str(fecha_nacimiento)+"'"
                       " , '"+str(genero_sexual)+"' , '"+str(contrasena_hash)+"')")


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
                cursor.execute("insert into usuario_has_usuario values (NULL , '" + str(self.correo_electronico) + "' , '" + str(
                    correo_amigo) + "')")
                cursor.execute("select idAmigo from usuario_has_usuario where usuario_CorreoElectronico = '" + str(
                    self.correo_electronico) + "' and usuario_CorreoElectronico1 = '" + str(correo_amigo) + "'")
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
            if item["usuario_CorreoElectronico"] == self.correo_electronico or item["usuario_CorreoElectronico"] == correo_amigo:
                if str(item["usuario_CorreoElectronico1"]) == str(correo_amigo) or item["usuario_CorreoElectronico1"] == self.correo_electronico:
                    id = item["IdAmigo"]
                    cursor.execute("delete from usuario_has_usuario where IdAmigo = (" + str(id) + ")")
                    for item in lista_amigos:
                        if (str(item.id_amigo) == str(id)):
                            lista_amigos.remove(item)
                            return lista_amigos
        return 0

    def crear_grupo (self , nomb , db):
        priv = 1
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select Nombre from grupo")
        mi_nombre = cursor.fetchall()
        for item in mi_nombre:
            if item["Nombre"] == str(nomb):
                return 0

        cursor.execute("insert into grupo values (NULL , '" + str(priv) + "' "
                       ", '" + str(nomb) + "' , '" + str(self.correo_electronico) + "')")
        cursor.execute("select idGrupo from grupo where Nombre = '" + str(nomb) + "' order by Nombre DESC")
        id = cursor.fetchall()
        print(id)
        id = id[0]["idGrupo"]

        cursor.execute("insert into grupoparticipa values (NULL , '" + str(priv) + "' "
                       ", '" + str(self.correo_electronico) + "' , '" + str(id) + "')")
        cursor.execute("select idGruposParticipa from grupoparticipa where grupo_nombre = '" + str(nomb) + "'" #ACA
                       "and usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'")
        id_grupo_participa = cursor.fetchall()
        id_grupo_participa = id_grupo_participa[0]["idGruposParticipa"]
        mi_grupo_participa = Grupo_participa()
        mi_grupo_participa.id_grupo_participa = id_grupo_participa
        mi_grupo_participa.nombre_grupo = nomb
        mi_grupo_participa.Administrador = 1
        mi_grupo_participa.correo_electronico = self.correo_electronico
        self.lista_grupos.append(mi_grupo_participa)
        return 1

    def crear_pagina (self , nomb , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("insert into pagina values (NULL ,'" + str(nomb) + "' , '" + str(self.correo_electronico) + "')")
        cursor.execute("select IdPagina from pagina where usuario_CorreoElectronico = "
                       "'" + str(self.correo_electronico) + "' and Nombre = '" + str(nomb) + "'")
        id = cursor.fetchall()
        id = id[0]["IdPagina"]

        cursor.execute("insert into paginaparticipa values (NULL , '" + str(id) + "' , 1 , '" + str(self.correo_electronico) + "')")
        cursor.execute("select idPaginasParticipa from paginaparticipa where Pagina_idPagina = '" + str(id) + "'"
                       "and usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'")
        id_pagina_participa = cursor.fetchall()
        id_pagina_participa = id_pagina_participa[0]["idPaginasParticipa"]
        mi_pagina_participa = Pagina_participa()
        mi_pagina_participa.id_pagina_participa = id_pagina_participa
        mi_pagina_participa.id_pagina = id
        mi_pagina_participa.Administrador = 1
        mi_pagina_participa.correo_electronico = self.correo_electronico
        self.lista_paginas.append(mi_pagina_participa)
        return 1

    def subir_multimedia (self , archivo , creacion , album , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_multimedia = Multimedia()
        #terminar
        cursor.execute("insert into Multimedia values (NULL , )")
        return 1

    def crear_post (self , fecha  , descripcion , id_pagina , id_grupo , id_archivo , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_post = Post()
        if id_pagina == 0 and id_grupo != 0:
            cursor.execute("insert into Post values (NULL , '" + str(fecha) + "' , '" + str(descripcion) + "' ,"
                           " '" + str(id_pagina) + "' , '" + str(self.correo_electronico) + "' , NULL)")
        elif id_pagina != 0 and id_grupo == 0:
            cursor.execute("insert into Post values (NULL , '" + str(fecha) + "' , '" + str(descripcion) + "' ,"
                           " NULL , '" + str(self.correo_electronico) + "' , '" + str(id_grupo) + "')")
        else:
            cursor.execute("insert into Post values (NULL , '" + str(fecha) + "' , '" + str(descripcion) + "' ,"
                           " NULL , '" + str(self.correo_electronico) + "' , NULL)")

        cursor.execute("select idPost from post where usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'"
                       "order by idPost DESC")
        id = cursor.fetchall()
        id = id[0]["idPost"]

        cursor.execute("insert into post_has_multimedia values ('" + str(id) + "' , '" + str(id_archivo) + "')")

        mi_post.id_post = id
        mi_post.fecha = fecha
        mi_post.descripcion = descripcion
        mi_post.id_pagina = id_pagina
        mi_post.id_grupo = id_grupo
        mi_post.archivos_multimedia = id_archivo
        self.lista_posts.append(mi_post)
        return 1

    def mandar_mensaje (self , id_amigo , mensaje , fecha , lista_usuarios , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_chat = Chat()

        cursor.execute("select usuario_CorreoElectronico from usuario_has_usuario where IdAmigo = '" + str(id_amigo) + "'")
        usuario_correo = cursor.fetchall()
        usuario_correo = usuario_correo[0]["usuario_CorreoElectronico"]
        if usuario_correo == self.correo_electronico:
            emisor = 1
        else:
            emisor = 0

        cursor.execute("insert into Chat values(NULL , '" + str(mensaje) + "' , '" + str(id_amigo) + "' , "
                       "'" + str(fecha) + "' , '" + str(emisor) + "')")
        cursor.execute("select idChat from Chat where usuario_has_usuario_IdAmigo = '" + str(id_amigo) + "' order by idChat DESC")
        id = cursor.fetchall()
        id = id[0]["idChat"]

        mi_chat.id_chat = id
        mi_chat.mensaje = mensaje
        mi_chat.id_amigo = id_amigo
        mi_chat.fecha = fecha
        mi_chat.emisor = emisor

        for item in self.lista_amigos:
            if item.id_amigo == id_amigo:
                item.conversacion.append(mi_chat)
        if emisor == 1:
            cursor.execute("select usuario_CorreoElectronico1 from usuario_has_usuario where IdAmigo = '" + str(id_amigo) + "'")
            correo_usuario_CorreoElectronico = cursor.fetchall()
            correo_usuario_CorreoElectronico = correo_usuario_CorreoElectronico[0]["usuario_CorreoElectronico1"]
        else:
            cursor.execute("select usuario_CorreoElectronico from usuario_has_usuario where IdAmigo = '" + str(id_amigo) + "'")
            correo_usuario_CorreoElectronico = cursor.fetchall()
            correo_usuario_CorreoElectronico = correo_usuario_CorreoElectronico[0]["usuario_CorreoElectronico"]

        for item in lista_usuarios:
            if item.correo_electronico == correo_usuario_CorreoElectronico:
                item.conversacion.append(mi_chat)
        return 1



    def suscribir_pagina (self , id_pagina , db):
        admin = "0"
        cursor = db.cursor(pymysql.cursors.DictCursor)
        mi_pagina = Pagina_participa()

        for item in self.lista_paginas:
            if item.correo_electronico == self.correo_electronico and item.id_pagina == id_pagina:
                return 0;

        cursor.execute("insert into paginaparticipa values (NULL , '" + str(id_pagina) + "' , '" + str(admin) + "' , '" + str(
            self.correo_electronico) + "')")
        cursor.execute("select idPaginasParticipa from paginaparticipa where Pagina_idPagina = '" + str(id_pagina) + "'"
                       "and usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'")
        id_pagina_participa = cursor.fetchall()
        id_pagina_participa = id_pagina_participa[0]["idPaginasParticipa"]
        mi_pagina_participa = Pagina_participa()
        mi_pagina_participa.id_pagina_participa = id_pagina_participa
        mi_pagina_participa.id_pagina = id
        mi_pagina_participa.Administrador = 1
        mi_pagina_participa.correo_electronico = self.correo_electronico
        self.lista_paginas.append(mi_pagina_participa)
        return 1

    def suscribir_grupo (self , id_grupo , db): #terminar de testear
        cursor = db.cursor(pymysql.cursors.DictCursor)
        admin = 0
        mi_grupo_participa = Grupo_participa()

        for item in self.lista_grupos:
            if item.correo_electronico == self.correo_electronico and item.id_grupo == id_grupo:
                return 0;

        cursor.execute("insert into grupoparticipa values (NULL , '" + str(admin) + "' , "
                       "'" + str(self.correo_electronico) + "' , '" + str(id_grupo) + "')")
        cursor.execute("select idGruposParticipa from grupoparticipa where idGrupo = '" + str(id_grupo) + "' and usuario_CorreoElectronico = "
                       "'" + str(self.correo_electronico) + "'")
        id = cursor.fetchall()
        id = id[0]["idGruposParticipa"]
        mi_grupo_participa.id_grupo_participa = id
        mi_grupo_participa.administrador = admin
        mi_grupo_participa.id_grupo = id_grupo
        mi_grupo_participa.correo_electronico = self.correo_electronico
        self.lista_grupos.append(mi_grupo_participa)
        return 1

        def desuscribir_pagina(self, id_pagina, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("delete from paginaparticipa where idPagina = '" + str(id_pagina) + "' and usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'")

        for item in self.lista_paginas:
            if item.id_pagina == id_pagina:
                self.lista_paginas.remove(item)
                return 1
        return 0

        def desuscribir_grupo(self, id_grupo, db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("delete from grupoparticipa where idGrupo = '" + str(id_grupo) + "' and usuario_CorreoElectronico = '" + str(self.correo_electronico) + "'")

        for item in self.lista_grupos:
            if item.id_grupo == id_grupo:
                self.lista_paginas.remove(item)
                return 1
        return 0

        def eliminar_grupo(self, id_grupo, lista_usuarios, db):
            cursor = db.cursor(pymysql.cursors.DictCursor)

            cursor.execute("select idGruposParticipa from grupoparticipa where idGrupo = '" + str(id_grupo) + "'")

            id = cursor.fetchall()
            id = id[0]["idGruposParticipa"]
            cursor.execute("delete from grupoparticipa where idGrupo = '" + str(id) + "'")
            cursor.execute("delete from grupo where idGrupo = '" + str(idGrupo) + "'")

            for item in lista_usuarios:
                for item2 in item.lista_grupos:
                    if item2.id_grupo == id_grupo:
                        item.lista_grupos.remove(item2)

            for item in self.lista_grupos:
                if item.id_grupo == id_grupo:
                    self.lista_paginas.remove(item)
                    return 1
            return 0

        def eliminar_pagina(self, id_pagina, lista_usuarios, db):
            cursor = db.cursor(pymysql.cursors.DictCursor)

            cursor.execute("select idPaginasParticipa from paginaparticipa where pagina_idPagina = '" + str(id_pagina) + "'")

            id = cursor.fetchall()
            id = id[0]["idPaginasParticipa"]
            cursor.execute("delete from paginaparticipa where idPagina = '" + str(id) + "'")
            cursor.execute("delete from pagina where idPagina = '" + str(idPagina) + "'")

            for item in lista_usuarios:
                for item2 in item.lista_paginas:
                    if item2.id_pagina == id_pagina:
                        item.lista_paginas.remove(item2)

            for item in self.lista_paginas:
                if item.id_pagina == id_pagina:
                    self.lista_paginas.remove(item)
                    return 1
            return 0