from datetime import date
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

while (True):
    tecla = input ("A (AGREGAR ALUMNO)\nB (AGREGAR PROFESOR)\nC (AGREGAR PLATO)\nD (AGREGAR PEDIDO) \n"
                   "E (MOFIDICAR PERSONA/PEDIDO/PLATO)\nF (ELIMINAR PERSONA/PEDIDO/PLATO)\n(m) mostrar todo\n\nRESPUESTA: ")

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
                            item.nombre = tecla

                        elif (tecla == "apellido"):
                            tecla = input("INGRESE EL NUEVO APELLIDO: ")
                            item.apellido = tecla

                        elif (tecla == "division"):
                            tecla = input("INGRESE EL NUEVO DIVISION: ")
                            item.division = tecla

                        elif (tecla == "dni"):
                            tecla = str (input("INGRESE EL NUEVO DNI: "))
                            item.dni = tecla

                        else:
                            print ("tecla incorrecta, intente nuevamente\n")



            elif (tecla == "b"):
                for mi_item in lista_personas:
                    if type(mi_item) is profesor:
                        print (mi_item.dni + "|" + mi_item.nombre + " " + mi_item.apellido + " - ")
                tecla = str (input("INGRESE EL DNI DEL PROFESOR: "))
                for item in lista_personas:
                    if (item.dni == tecla):
                        tecla = input("INGRESE LO QUE DESEA MODIFICAR (NOMBRE/APELLIDO/DESCUENTO/DNI): ")
                        if (tecla == "nombre"):
                            tecla = input("INGRESE EL NUEVO NOMBRE: ")
                            item.nombre = tecla

                        elif (tecla == "apellido"):
                            tecla = input("INGRESE EL NUEVO APELLIDO: ")
                            item.apellido = tecla

                        elif (tecla == "descuento"):
                            tecla = int (input("INGRESE EL NUEVO DESCUENTO: "))
                            item.descuento = tecla

                        elif (tecla == "dni"):
                            tecla = str (input("INGRESE EL NUEVO DNI: "))
                            item.dni = tecla

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
                            item.nombre = tecla

                        elif (tecla == "precio"):
                            tecla = int (input("INGRESE EL NUEVO PRECIO: "))
                            item.precio = tecla

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
                                item.estado = "entregado"
                            elif (tecla == "en proceso"):
                                item.estado = "en proceso"

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

        lista_personas.append (mi_alumno)

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

        lista_personas.append(mi_profesor)

    elif (tecla == "c"):
        mi_plato = plato ()
        tecla = input("ESCRIBA EL NOMBRE DEL PLATO: ")
        mi_plato.agregar_nombre(str (tecla))

        tecla = input("ESCRIBA EL PRECIO DEL PLATO: ")
        mi_plato.agregar_precio (int (tecla))

        lista_platos.append (mi_plato)

    elif (tecla == "d"):
        mi_pedido = pedido ()
        dia = int (input("ESCRIBA EL DIA DE CREACION DEL PEDIDO: "))
        mes = int (input("ESCRIBA EL MES DE CREACION DEL PEDIDO: "))
        ano = int (input("ESCRIBA EL AÑO DE CREACION DEL PEDIDO: "))
        mi_pedido.agregar_fecha_creacion (date (ano , mes , dia))

        for mi_item in lista_platos:
            print (mi_item.nombre + " - ")
        tecla = input("ESCRIBA EL NOMBRE DEL PLATO A PEDIR: ")
        for item in lista_platos:
            if (item.nombre == tecla):
                mi_pedido.agregar_plato(item)

        for mi_item in lista_personas:
            print (mi_item.dni + "|" + mi_item.nombre + " " + mi_item.apellido + " - ")
        tecla = input("ESCRIBA EL DNI DE LA PERSONA QUE PIDIO EL PLATO: ")
        for item in lista_personas:
            if (item.dni == tecla):
                mi_pedido.agregar_persona (item)

        tecla = str (input("ESCRIBA LA HORA DE ENTREGA DEL PEDIDO: "))
        mi_pedido.agregar_hora_entrega (tecla)

        mi_pedido.establecer_estado ("en proceso")
        mi_pedido.establecer_nro_pedido(nro_pedido)
        nro_pedido += 1

        lista_pedidos.append (mi_pedido)

    elif (tecla == "m"):
        print ("\nPEDIDOS: \n")
        for item in lista_pedidos:
            print ("\nNRO. PEDIDO: " + str (item.nro_pedido) + "\nCREACION: " + str (item.fecha_creacion) + "\nPERSONA: "
                   + str (item.persona.dni) + "\nDESCUENTO DE LA PERSONA: " + str (item.persona.dar_desc ()) + "\nNOMBRE PLATO: "
                   + str (item.plato.nombre) + "\nPRECIO PLATO: " + str (item.plato.precio) + "\nPRECIO PLATO CON DESCUENTO: "
                   + str (int (item.plato.precio) - ((int (item.plato.precio) / 100) * int (item.persona.dar_desc ()))) + "\nHORA ENTREGA: "
                   + str (item.hora_entrega + "\nESTADO PEDIDO: " + item.estado))

        print ("PERSONAS: \n")
        for item in lista_personas:
            print ("dni: " + str (item.dni) + " | nombre comp: " + str (item.nombre) + " " + str (item.apellido)
                    + " | desc: " + str (item.descuento) + "\n")

        print ("PLATOS: \n")
        for item in lista_platos:
            print ("nombre: " + str (item.nombre) + " | precio: " + str (item.precio) + "\n")

    else:
        print ("tecla incorrecta, intente nuevamente\n")