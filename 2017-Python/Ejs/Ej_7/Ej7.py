from datetime import date
from ....Clases.ej7.ej7alumno import alumno
from ....Clases.ej7.ej7pedido import pedido
from ....Clases.ej7.ej7plato import plato
from ....Clases.ej7.ej7profesor import profesor

mi_alumno = alumno ()
mi_profesor = profesor ()
mi_plato = plato ()
mi_pedido = pedido ()
lista_pedidos = []
lista_personas = []
lista_platos = []
tecla = None
dia = None
mes = None
ano = None
nro_pedido = 0

tecla = input ("A (AGREGAR_ALUMNO)\nB (AGREGAR PROFESOR)\nC (AGREGAR PLATO)\nD (AGREGAR PEDIDO) \nE (CAMBIAR ESTADO DEL PEDIDO)")

while (True):
    if (tecla == "A"):
        tecla = input("ESCRIBA EL NOMBRE DEL ALUMNO: ")
        mi_alumno.agregar_nombre(str (tecla))

        tecla = input("ESCRIBA EL APELLIDO DEL ALUMNO: ")
        mi_alumno.agregar_apellido(str (tecla))

        tecla = input("ESCRIBA LA DIVISION DEL ALUMNO: ")
        mi_alumno.agregar_division(str (tecla))

        lista_personas.append (mi_alumno)

    elif (tecla == "B"):
        tecla = input("ESCRIBA EL NOMBRE DEL PROFESOR: ")
        mi_profesor.agregar_nombre(str (tecla))

        tecla = input("ESCRIBA EL APELLIDO DEL PROFESOR: ")
        mi_profesor.agregar_apellido(str (tecla))

        tecla = input("ESCRIBA EL DESCUENTO DEL PROFESOR: ")
        mi_profesor.agregar_desc (int (tecla))

        lista_personas.append(mi_profesor)

    elif (tecla == "c"):
        tecla = input("ESCRIBA EL NOMBRE DEL PLATO: ")
        mi_plato.agregar_nombre(str (tecla))

        tecla = input("ESCRIBA EL PRECIO DEL PLATO: ")
        mi_plato.agregar_precio (int (tecla))

        lista_platos.append (mi_plato)

    elif (tecla == "d"):
        dia = int (input("ESCRIBA EL DIA DE CREACION DEL PEDIDO: "))
        mes = int (input("ESCRIBA EL MES DE CREACION DEL PEDIDO: "))
        ano = int (input("ESCRIBA EL AÑO DE CREACION DEL PEDIDO: "))
        mi_pedido.agregar_fecha_creacion (date (ano , mes , dia))

        tecla = input("ESCRIBA EL NOMBRE DEL PLATO A PEDIR: ")
        for item in lista_platos:
            if (item.nombre == tecla):
                mi_pedido.agregar_plato(item)

        tecla = input("ESCRIBA EL NOMBRE COMPLETO DE LA PERSONA QUE PIDIO EL PLATO: ")
        for item in lista_personas:
            if ((item.nombre + " " + item.apellido) == tecla):
                mi_pedido.agregar_persona (item)

        tecla = int (input("ESCRIBA LA HORA DE ENTREGA DEL PEDIDO: "))
        mi_pedido.agregar_hora_entrega (str (tecla))

        mi_pedido.establecer_estado ("en proceso")
        mi_pedido.establecer_nro_pedido(nro_pedido)
        nro_pedido += 1

        lista_pedidos.append (mi_pedido)

    elif (tecla == "e"):
        tecla = str (input ("INGRESE EL NUMERO DE PEDIDO A MODIFICAR: "))

        for item in lista_pedidos:
            if (item.nro_pedido == tecla):
                tecla = str (input ("INGRESE EL NUEVO ESTADO DEL PEDIDO ('EN PROCESO' , 'ENTREGADO'): "))
                item.establecer_estado (tecla)

    else:
        print ("tecla incorrecta, intente nuevamente\n")


