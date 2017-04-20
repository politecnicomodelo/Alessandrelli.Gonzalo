from datetime import date
from Clases.empresa import empresa
from Clases.empleado import empleado

mi_empresa = empresa ()
mi_empleado = empleado ()
cantidad_empleados = 0;
dias_labor = 0
dia = None
mes = None
ano = None
hora = None
identificador = 0

mi_empresa.set_nombre (str(input ("INGRESE EL NOMBRE DE LA EMPRESA: ")))
mi_empresa.set_telefono (input ("INGRESE EL NUMERO DE TELEFONO DE LA EMPRESA: "))

cantidad_empleados = input ("CUANTOS EMPLEADOS TIENE ESTA EMPRESA: ")

for i in range (int(cantidad_empleados) + 1):
    mi_empleado.set_nombre (input ("INGRESE EL NOMBRE DEL EMPLEADO: "))
    mi_empleado.set_apellido (input("INGRESE EL APELLIDO DEL EMPLEADO: "))
    mi_empleado.set_telefono (input("INGRESE EL NUMERO DE TELEFONO DEL EMPLEADO: "))
    dia = input("DIA DE CUMPLEAÑOS (NUMERICAMENTE): ")
    mes = input("MES DE CUMPLEAÑOS (NUMERICAMENTE): ")
    ano = input("ANO DE CUMPLEAÑOS (NUMERICAMENTE): ")
    mi_empleado.set_fecha_nacimiento (int (dia) , int (mes) , int (ano))
    dias_labor = input ("INGRESE CANTIDAD DE DIAS A TRABAJAR POR SEMANA (MAX 5 , MIN 1): ")
    for i in range (int(dias_labor) + 1):
        mi_empleado.dias_de_labor (input ("INGRESE UN DIA DE LA SEMANA A TRABAJAR (0/1/2/3/4 SIENDO 0 LUNES Y 4 VIERNES): "))
    mi_empleado.set_idenficador (identificador)
    identificador += 1
    print ("asistencias: ")
    for i in range(4):
        dia = input("DIA DE CUMPLEAÑOS (NUMERICAMENTE): ")
        mes = input("MES DE CUMPLEAÑOS (NUMERICAMENTE): ")
        ano = input("ANO DE CUMPLEAÑOS (NUMERICAMENTE): ")
        hora = str (input("HORA DE CUMPLEAÑOS (FORMATO 24HS): "))
        datos = [ano , mes , dia , hora]
        mi_empleado.asistencia (datos)
    mi_empresa.agregar_empleado (mi_empleado)

    mi_empresa.calcular_porcentaje_asistencias (input ("INGRESE EL IDENTIFICADOR DEL EMPLEADO: "))