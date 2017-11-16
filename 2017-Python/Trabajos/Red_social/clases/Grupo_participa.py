import pymysql
from datetime import date

class Grupo_participa (object):
    id_grupo_participa = None
    administrador = None
    id_grupo = None
    id_usuario = None
    estado_invitacion = None

    def agregar_participante_grupo(self, mi_id_usuario , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(
            "select administrador from grupoparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (str(check[0]["administrador"]) == "1")):
            cursor.execute("select estadoinvitacion from grupoparticipa where usuario_idusuario = "
                           "'" + str(id_usuario) + "' and idgrupo = '" + str(self.id_grupo_participa) + "'")
            estado = cursor.fetchall()

            estado = estado[0]["estadoinvitacion"]

            if estado == "pendiente":
                cursor.execute("update grupoaparticipa set estadoinvitacion = '" + "integrante" + "'")
                return 1
        return 0

    def eliminar_participante_grupo(self , mi_id_usuario , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("select usuario_idusuario from grupo where idgrupo = '" + str(self.id_grupo_participa) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (str(check[0]["usuario_idusuario"]) != id_usuario)):

            cursor.execute(
                "select administrador from grupoparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
            check = cursor.fetchall()

            if ((check != ()) and (str(check[0]["administrador"]) == "1")):
                cursor.execute("select estadoinvitacion from grupoparticipa where usuario_idusuario = "
                               "'" + str(id_usuario) + "' and idgrupo = '" + str(self.id_grupo_participa) + "'")
                estado = cursor.fetchall()

                estado = estado[0]["estadoinvitacion"]

                if estado == "integrante":
                    cursor.execute("select usuario_idusuario from grupo where idgrupo = '" + str(self.id_grupo_participa) + "'")
                    id = cursor.fetchall()
                    id = id[0]["usuario_idusuario"]
                    if id != mi_id_usuario:
                        cursor.execute("delete from grupoaparticipa where usuario_idusuario = "
                                       "'" + str(id_usuario) + "' and idgrupo = '" + str(self.id_grupo_participa) + "'")
                        return 1
        elif ((check != ()) and (str(check[0]["usuario_idusuario"]) == id_usuario)):
            return 0, "el usuario que se intento eliminar es el administrador principal"
        return 0


    def hacer_admin_grupo(self , mi_id_usuario , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(
            "select administrador from grupoparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (check[0]["administrador"] == 1)):
            return 0, "el usuario ya es un administrador"

            if ((check != ()) and (str(check[0]["administrador"]) == "0")):
                cursor.execute("update grupoparticipa set administrador = '" + str("1") + "' where usuario_idusuario"
                               " = '" + str(id_usuario) + "' and grupo_idgrupo = '" + str(self.id_grupo_participa) + "'")
                return 1
        return 0

    def deshacer_admin_grupo(self, mi_id_usuario , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(
            "select administrador from grupoparticipa where usuario_idusuario = '" + str(mi_id_usuario) + "'")
        check = cursor.fetchall()

        if ((check != ()) and (check[0]["administrador"] == 1)):
            cursor.execute(
                "select administrador from grupoparticipa where usuario_idusuario = '" + str(self.id_grupo_participa) + "'"
                " and grupo_idgrupo = '" + str(self.id_grupo_participa) + "'")
            check = cursor.fetchall()

            if ((check != ()) and (str(check[0]["administrador"]) == "1")):
                cursor.execute("update grupoparticipa set administrador = '" + str("1") + "' where usuario_idusuario"
                                                                                          " = '" + str(
                    id_usuario) + "' and grupo_idgrupo = '" + str(self.id_grupo_participa) + "'")
                return 1
        return 0

    def eliminar_grupo(self , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("select idGruposParticipa from grupoparticipa where idGrupo = '" + str(self.id_grupo_participa) + "'")

        id = cursor.fetchall()
        id = id[0]["idGruposParticipa"]
        cursor.execute("delete from grupoparticipa where idGrupo = '" + str(id) + "'")
        cursor.execute("delete from grupo where idGrupo = '" + str(self.id_grupo_participa) + "'")
        return 1

    def crear_grupo (self , nomb , priv , id_usuario , db):
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("insert into grupo values (NULL , '" + str(priv) + "' "
                       ", '" + str(nomb) + "' , '" + str(id_usuario) + "')")

        cursor.execute("select idGrupo from grupo where Nombre = '" + str(nomb) + "' order by Nombre DESC")
        id = cursor.fetchall()
        id = id[0]["idGrupo"]

        cursor.execute("insert into grupoparticipa values (NULL , '" + "1" + "' "
                       ", '" + str(self.id_usuario) + "' , '" + str(id) + "' , '" + "1" + "')")

        cursor.execute("select idGruposParticipa from grupoparticipa where grupo_idgrupo = '" + str(id) + "'"
                       "and usuario_idusuario = '" + str(id_usuario) + "'")
        id_grupo_participa = cursor.fetchall()
        id_grupo_participa = id_grupo_participa[0]["idGruposParticipa"]

        mi_grupo_participa = Grupo_participa()
        mi_grupo_participa.id_grupo_participa = id_grupo_participa
        mi_grupo_participa.nombre_grupo = nomb
        mi_grupo_participa.Administrador = 1
        mi_grupo_participa.id_usuario = id_usuario
        mi_grupo_participa.estado_invitacion = 0

        return mi_grupo_participa