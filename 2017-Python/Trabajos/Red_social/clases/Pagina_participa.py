import pymysql
from datetime import date

class Pagina_participa (object):
    id_pagina_participa = None
    id_pagina = None
    administrador = None
    id_ususario = None

    def aceptar_post_pagina(self , id_post , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.update("update post set aceptacion = 2 where idpost = '" + str(id_post) + "' and "
                      "pagina_idpagina = '" + str(self.id_pagina_participa) + "'")

    def declinar_post_pagina(self, id_post , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.update("update post set aceptacion = 1 where idpost = '" + str(id_post) + "' and "
                      "pagina_idpagina = '" + str(self.id_pagina_participa) + "'")

    def hacer_admin_pagina (self , mi_id_usuario , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("select administrador from paginaparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (check[0]["administrador"] == 1)):
            return 0 , "el usuario ya es administrador"

            if ((check != ()) and (str(check[0]["administrador"]) == "0")):
                cursor.execute("update paginaparticipa set administrador = '" + str("1") + "' where usuario_idusuario"
                               " = '" + str(id_usuario) + "' and pagina_idpagina = '" + str(self.id_pagina_participa) + "'")
                return 1
        return 0

    def deshacer_admin_pagina(self , mi_id_usuario ,  id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(
            "select administrador from grupoparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (check[0]["administrador"] == 1)):
            cursor.execute(
                "select administrador from paginaparticipa where usuario_idusuario = '" + str(self.id_pagina_participa) + "'"
                " and pagina_idpagina = '" + str(self.id_pagina_participa) + "'")
            check = cursor.fetchall()

            if ((check != ()) and (str(check[0]["administrador"]) == "1")):
                cursor.execute("update paginaparticipa set administrador = '" + str("0") + "' where usuario_idusuario"
                               " = '" + str(id_usuario) + "' and pagina_idpagina = '" + str(self.id_pagina_participa) + "'")
                return 1
        return 0

    def eliminar_pagina(self , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("select idPaginasParticipa from paginaparticipa where pagina_idPagina = '" + str(self.id_pagina_participa) + "'")

        id = cursor.fetchall()
        id = id[0]["idPaginasParticipa"]
        cursor.execute("delete from paginaparticipa where idPagina = '" + str(id) + "'")
        cursor.execute("delete from pagina where idPagina = '" + str(self.id_pagina_participa) + "'")
        return 1

    def crear_pagina (self , mi_id_usuario , nomb , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("insert into pagina values (NULL , '" + str(nomb) + "' , '" + str(mi_id_usuario) + "')")

        cursor.execute("select idPagina from Pagina where Nombre = '" + str(nomb) + "' order by Nombre DESC")
        id = cursor.fetchall()
        id = id[0]["idPagina"]

        cursor.execute("insert into paginaparticipa values (NULL , '" + str(id) + "' , '" + "1" + "' "
                       ", '" + str(mi_id_usuario) + "')")
        return 1
