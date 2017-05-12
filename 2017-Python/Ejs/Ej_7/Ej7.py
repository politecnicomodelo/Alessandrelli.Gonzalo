from datetime import date
from datetime import datetime
from clases.ej7alumno import alumno
from clases.ej7pedido import pedido
from clases.ej7plato import plato
from clases.ej7profesor import profesor

lista_pedidos = []
lista_personas = []
lista_platos = []
tecla = None
dia = None
mes = None
ano = None
nro_pedido = 0
dato = []

arc_alumnos = open ("arc_alumnos.txt", "r")
for line in arc_alumnos:
    if (line == ""):
        break
    mi_alumno = alumno()
    dato = line.split('º')
    mi_alumno.agregar_dni (dato [0])
    mi_alumno.agregar_nombre (dato [1])
    mi_alumno.agregar_apellido (dato [2])
    mi_alumno.agregar_division (dato [3])

    lista_personas.append (mi_alumno)
arc_alumnos.close()

arc_profesores = open ("arc_profesores.txt", "r")
for line in arc_profesores:
    if (line == ""):
        break
    mi_profesor = profesor()
    dato = line.split('º')
    mi_profesor.agregar_dni (dato [0])
    mi_profesor.agregar_nombre (dato [1])
    mi_profesor.agregar_apellido (dato [2])
    mi_profesor.agregar_desc (dato [3])
    lista_personas.append (mi_profesor)
arc_profesores.close()

arc_platos = open ("arc_platos.txt", "r")
for line in arc_platos:
    if (line == ""):
        break
    mi_plato = plato()
    dato = line.split('º')
    mi_plato.agregar_nombre (dato [0])
    mi_plato.agregar_precio (dato [1])
    lista_platos.append (mi_plato)
arc_platos.close()

arc_pedidos = open ("arc_pedidos.txt", "r")
for line in arc_pedidos:
    if (line == ""):
        break
    mi_pedido = pedido()
    dato = line.split('º')
    mi_pedido.establecer_nro_pedido (dato [0])
    for item in lista_personas:
        if (item.dni == dato [1]):
            mi_pedido.agregar_persona (item)
    for item in lista_platos:
        if (item.nombre == dato [2]):
            mi_pedido.agregar_plato (item)
    mi_pedido.agregar_hora_entrega (dato [3])
    mi_pedido.establecer_estado (int (dato [4]))
    dato = dato [5].split('-')
    mi_pedido.agregar_fecha_creacion (date (int (dato [0]) , int (dato [1]) , int (dato [2])))
    lista_pedidos.append (mi_pedido)
arc_pedidos.close()

nro_pedido = (int (lista_pedidos [-1].nro_pedido) + 1)



while (True):
    tecla = input ("A (AGREGAR ALUMNO)\nB (AGREGAR PROFESOR)\nC (AGREGAR PLATO)\nD (AGREGAR PEDIDO) \n"
                   "E (MOFIDICAR PERSONA/PEDIDO/PLATO)\nF (ELIMINAR PERSONA/PEDIDO/PLATO)\nP "
                   "(MOSTRAR PEDIDOS DEL DIA)\nG (GUARDAR TODO)\nm (mostrar todo)\n\nRESPUESTA: ")

    if (tecla == "e"):
        while (True):
            tecla = input ("A (MODIFICAR ALUMNO)\nB (MODIFICAR PROFESOR)\nC (MODIFICAR PLATO)\n"
                           "D (MODIFICAR ESTADO PEDIDO)\nS (salir)\n\nRESPUESTA: ")

            if (tecla == "s"):
                break
            elif (tecla == "a"):
                for mi_item in lista_personas:
                    if type (mi_item) is alumno:
                        print (mi_item.dni + "|" + mi_item.nombre + " " + mi_item.apellido + " - ")
                tecla = str (input ("INGRESE EL DNI DEL ALUMNO: "))
                for item in lista_personas:
                    if (item.dni == tecla):
                        tecla = input ("INGRESE LO QUE DESEA MODIFICAR (NOMBRE/APELLIDO/DIVISION/DNI): ")
                        if (tecla == "nombre"):
                            tecla = input ("INGRESE EL NUEVO NOMBRE: ")
                            item.agregar_nombre (tecla)

                        elif (tecla == "apellido"):
                            tecla = input("INGRESE EL NUEVO APELLIDO: ")
                            item.agregar_apellido (tecla)

                        elif (tecla == "division"):
                            tecla = input("INGRESE EL NUEVO DIVISION: ")
                            item.agregar_division (tecla)

                        elif (tecla == "dni"):
                            tecla = str (input("INGRESE EL NUEVO DNI: "))
                            item.agregar_dni (tecla)

                        else:
                            print ("tecla incorrecta, intente nuevamente\n")



            elif (tecla == "b"):
                for mi_item in lista_personas:
                    if type(mi_item) is profesor:
                        print (str (mi_item.dni) + "|" + str (mi_item.nombre + " " + mi_item.apellido) + " - ")
                tecla = str (input("INGRESE EL DNI DEL PROFESOR: "))
                for item in lista_personas:
                    if (item.dni == tecla):
                        tecla = input("INGRESE LO QUE DESEA MODIFICAR (NOMBRE/APELLIDO/DESCUENTO/DNI): ")
                        if (tecla == "nombre"):
                            tecla = input("INGRESE EL NUEVO NOMBRE: ")
                            item.agregar_nombre (tecla)

                        elif (tecla == "apellido"):
                            tecla = input("INGRESE EL NUEVO APELLIDO: ")
                            item.agregar_apellido (tecla)

                        elif (tecla == "descuento"):
                            tecla = int (input("INGRESE EL NUEVO DESCUENTO: "))
                            item.agregar_descuento (tecla)

                        elif (tecla == "dni"):
                            tecla = str (input("INGRESE EL NUEVO DNI: "))
                            item.agregar_dni (tecla)

                        else:
                            print ("tecla incorrecta, intente nuevamente\n")



            elif (tecla == "c"):
                for mi_item in lista_platos:
                    print (mi_item.nombre + " - ")
                tecla = input("INGRESE EL NOMBRE DEL PLATO: ")
                for item in lista_platos:
                    if (item.nombre == tecla):
                        tecla = input("INGRESE LO QUE DESEA MODIFICAR (NOMBRE/PRECIO): ")
                        if (tecla == "nombre"):
                            tecla = str (input("INGRESE EL NUEVO NOMBRE: "))
                            item.agregar_nombre (tecla)

                        elif (tecla == "precio"):
                            tecla = int (input("INGRESE EL NUEVO PRECIO: "))
                            item.agregar_precio (tecla)

                        else:
                            print ("tecla incorrecta, intente nuevamente\n")

            elif (tecla == "d"):
                for mi_item in lista_pedidos:
                    print (str (mi_item.nro_pedido) + " - ")
                tecla = int (input("INGRESE EL NUMERO DEL PEDIDO: "))
                for item in lista_pedidos:
                    if (item.nro_pedido == tecla):
                        tecla = input("INGRESE EL NUEVO ESTADO DEL PEDIDO (ENTREGADO/EN PROCESO)): ")
                        if (tecla == "entregado"):
                            if (tecla == "entregado"):
                                item.establecer_estado (1)
                            elif (tecla == "en proceso"):
                                item.establecer_estado (0)

            elif (tecla == "s"):
                break

            else:
                print ("tecla incorrecta, intente nuevamente\n")


    elif (tecla == "f"):
        while (True):
            tecla = input ("A (ELIMINAR PERSONA)\nB (ELIMINAR PLATO)\nC (ELIMINAR PEDIDO)\nS (salir)\n\nRESPUESTA: ")

            if (tecla == "a"):
                for mi_item in lista_personas:
                    print (mi_item.dni + "|" + mi_item.nombre + " " + mi_item.apellido + " - ")
                tecla = str (input("INGRESE EL DNI DE LA PERSONA: "))
                for item in lista_personas:
                    if (item.dni == tecla):
                        lista_personas.remove (item)

            elif (tecla == "b"):
                for mi_item in lista_platos:
                    print (mi_item.nombre + " - ")
                tecla = str(input("INGRESE EL NOMBRE DEL PLATO: "))
                for item in lista_platos:
                    if (item.nombre == tecla):
                        lista_platos.remove(item)

            elif (tecla == "c"):
                for mi_item in lista_pedidos:
                    print (mi_item.nro_pedido + " - ")
                tecla = int (input("INGRESE EL NUMERO DE PEDIDO: "))
                for item in lista_pedidos:
                    if (item.nro_pedido == tecla):
                        lista_pedidos.remove(item)

            elif (tecla == "s"):
                break

            else:
                print ("tecla incorrecta, intente nuevamente\n")




    elif (tecla == "a"):
        mi_alumno = alumno ()
        tecla = str (input("ESCRIBA EL NOMBRE DEL ALUMNO: "))
        mi_alumno.agregar_nombre (tecla)

        tecla = str (input("ESCRIBA EL APELLIDO DEL ALUMNO: "))
        mi_alumno.agregar_apellido (tecla)

        tecla = str (input("ESCRIBA LA DIVISION DEL ALUMNO: "))
        mi_alumno.agregar_division (tecla)

        tecla = str (input("ESCRIBA EL DNI DEL ALUMNO: "))
        mi_alumno.agregar_dni (tecla)
        for item in lista_personas:
            if (item.dni == mi_alumno.dni):
                print ("ESE DNI ESTA EN USO\n")
                break
            lista_personas.append(mi_alumno)


    elif (tecla == "b"):
        mi_profesor = profesor ()
        tecla = str (input("ESCRIBA EL NOMBRE DEL PROFESOR: "))
        mi_profesor.agregar_nombre (tecla)

        tecla = str (input("ESCRIBA EL APELLIDO DEL PROFESOR: "))
        mi_profesor.agregar_apellido (tecla)

        tecla = int (input("ESCRIBA EL DESCUENTO DEL PROFESOR: "))
        mi_profesor.agregar_desc (tecla)

        tecla = str (input("ESCRIBA EL DNI DEL PROFESOR: "))
        mi_profesor.agregar_dni (tecla)

        for item in lista_personas:
            if (item.dni == mi_profesor.dni):
                print ("ESE DNI ESTA EN USO\n")
                break
            lista_personas.append(mi_profesor)


    elif (tecla == "c"):
        mi_plato = plato ()
        tecla = input("ESCRIBA EL NOMBRE DEL PLATO: ")
        mi_plato.agregar_nombre(str (tecla))

        tecla = input("ESCRIBA EL PRECIO DEL PLATO: ")
        mi_plato.agregar_precio (int (tecla))

        for item in lista_platos:
            if (item.nombre == mi_plato.nombre):
                print ("ESE NOMBRE ESTA EN USO\n")
                break
            lista_platos.append(mi_plato)

    elif (tecla == "d"):
        mi_pedido = pedido ()
        dia = int (input("ESCRIBA EL DIA DE CREACION DEL PEDIDO: "))
        mes = int (input("ESCRIBA EL MES DE CREACION DEL PEDIDO: "))
        ano = int (input("ESCRIBA EL ANO DE CREACION DEL PEDIDO: "))
        mi_pedido.agregar_fecha_creacion (date (ano , mes , dia))

        while (True):
            for mi_item in lista_platos:
                print (mi_item.nombre + " - ")
            tecla = input("ESCRIBA EL NOMBRE DEL PLATO A PEDIR: ")
            for item in lista_platos:
                if (item.nombre == tecla):
                    mi_pedido.agregar_plato(item)

            if (mi_pedido.plato == None):
                print ("ESE PLATO NO EXISTE, REINGRESE EL DATO:\n")
            else:
                break

        while (True):
            for mi_item in lista_personas:
                print (mi_item.dni + "|" + mi_item.nombre + " " + mi_item.apellido + " - ")
            tecla = input("ESCRIBA EL DNI DE LA PERSONA QUE PIDIO EL PLATO: ")
            for item in lista_personas:
                if (item.dni == tecla):
                    mi_pedido.agregar_persona (item)

            if (mi_pedido.persona == None):
                print ("ESE DNI NO EXISTE, REINGRESE EL DATO:\n")
            else:
                break

        tecla = str (input("ESCRIBA LA HORA DE ENTREGA DEL PEDIDO: "))
        mi_pedido.agregar_hora_entrega (tecla)

        mi_pedido.establecer_estado (0)
        mi_pedido.establecer_nro_pedido(nro_pedido)
        nro_pedido += 1

        lista_pedidos.append (mi_pedido)

    elif (tecla == "p"):

        print ("PEDIDOS DEL DIA:\n")

        for item in lista_pedidos:
            if ((item.fecha_creacion == datetime.today().date()) and (item.estado == 0)):
                print ("PEDIDO:\nNRO_PEDIDO: " + str (item.nro_pedido) + "\nHORA DE ENTREGA: " + str (item.hora_entrega)
                       + "\nPLATO: " + str (item.plato.nombre) + "\nPRECIO CON DESCUENTO: $" + str (item.dar_precio_con_desc()))


    elif (tecla == "m"):
        print ("\nPEDIDOS: \n")
        for item in lista_pedidos:
            print (item)

        print ("PERSONAS: \n")
        for item in lista_personas:
            print (item)

        print ("PLATOS: \n")
        for item in lista_platos:
            print (item)

    elif (tecla == "g"):
        arc_alumnos = open("arc_alumnos.txt" , "w")
        for item in lista_personas:
            if (type (item) is alumno):
                arc_alumnos.write(str(item.dni) + "º")
                arc_alumnos.write(str(item.nombre) + "º")
                arc_alumnos.write(str(item.apellido) + "º")
                arc_alumnos.write(str(item.division) + "º" + "\n")
        arc_alumnos.close()

        arc_profesores = open("arc_profesores.txt", "w")
        for item in lista_personas:
            if (type (item) is profesor):
                arc_profesores.write(str(item.dni) + "º")
                arc_profesores.write(str(item.nombre) + "º")
                arc_profesores.write(str(item.apellido) + "º")
                arc_profesores.write(str(item.descuento) + "º" + "\n")
        arc_profesores.close()

        arc_plato = open("arc_platos.txt", "w")
        for item in lista_platos:
            arc_plato.write(str(item.nombre) + "º")
            arc_plato.write(str(item.precio) + "º" + "\n")
        arc_plato.close()

        arc_pedidos = open("arc_pedidos.txt" , "w")
        for item in lista_pedidos:
            arc_pedidos.write(str(item.nro_pedido) + "º")
            arc_pedidos.write(str(item.persona.dni) + "º")
            arc_pedidos.write(str(item.plato.nombre) + "º")
            arc_pedidos.write(str(item.hora_entrega) + "º")
            arc_pedidos.write(str(item.estado) + "º")
            arc_pedidos.write(str(item.fecha_creacion) + "º" + "\n")
        arc_pedidos.close()


    else:
        print ("tecla incorrecta, intente nuevamente\n")





    def cargar_datos (nro_pedido , lista_personas , lista_platos , lista_pedidos):
        arc_alumnos = open("arc_alumnos.txt", "r")
        for line in arc_alumnos:
            if (line == ""):
                break
            mi_alumno = alumno()
            dato = line.split('º')
            mi_alumno.agregar_dni(dato[0])
            mi_alumno.agregar_nombre(dato[1])
            mi_alumno.agregar_apellido(dato[2])
            mi_alumno.agregar_division(dato[3])

            lista_personas.append(mi_alumno)
        arc_alumnos.close()

        arc_profesores = open("arc_profesores.txt", "r")
        for line in arc_profesores:
            if (line == ""):
                break
            mi_profesor = profesor()
            dato = line.split('º')
            mi_profesor.agregar_dni(dato[0])
            mi_profesor.agregar_nombre(dato[1])
            mi_profesor.agregar_apellido(dato[2])
            mi_profesor.agregar_desc(dato[3])
            lista_personas.append(mi_profesor)
        arc_profesores.close()

        arc_platos = open("arc_platos.txt", "r")
        for line in arc_platos:
            if (line == ""):
                break
            mi_plato = plato()
            dato = line.split('º')
            mi_plato.agregar_nombre(dato[0])
            mi_plato.agregar_precio(dato[1])
            lista_platos.append(mi_plato)
        arc_platos.close()

        arc_pedidos = open("arc_pedidos.txt", "r")
        for line in arc_pedidos:
            if (line == ""):
                break
            mi_pedido = pedido()
            dato = line.split('º')
            mi_pedido.establecer_nro_pedido(dato[0])
            for item in lista_personas:
                if (item.dni == dato[1]):
                    mi_pedido.agregar_persona(item)
            for item in lista_platos:
                if (item.nombre == dato[2]):
                    mi_pedido.agregar_plato(item)
            mi_pedido.agregar_hora_entrega(dato[3])
            mi_pedido.establecer_estado(int(dato[4]))
            dato = dato[5].split('-')
            mi_pedido.agregar_fecha_creacion(date(int(dato[0]), int(dato[1]), int(dato[2])))
            lista_pedidos.append(mi_pedido)
        arc_pedidos.close()

        nro_pedido = (int(lista_pedidos[-1].nro_pedido) + 1)