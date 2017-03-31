from datetime import date
from .materia import materia


#ERRORRES: AGREGARNOTA DEBERIA ESTAR EN MATERIA, AL IGUAL ME CON PROMEDIO, PROMEDIONOTASMATERIA, ENOR PROMEDIO, AGREGAR NOTA.
#ESTA MAL PLANTEADO YA QUE LOS ALUMNOS DEBERIAN ESTAR DENTR DE LAS MATERIAS Y NO DE REVEZ.
#ESTOS SON ERRORES PORQUE PRODUCEN COHECION.


class alumno (object):

    Nombre = ""
    Apellido = ""
    FechaDeNacimiento = None
    ListaMaterias = []

    def __init__(self):
        self.ListaMaterias = []

    def SetNombre (self , n):
        self.nombre = n

    def SetApellido (self , a):
        self.apellido = a

    def SetFechaNacimiento (self , a , m , d):
        self.FechaDeNacimiento = date (a,m,d)

    def AgregarMateria (self , m):
        Materia = materia ()
        Materia.nombre = m
        self.ListaMaterias.append (Materia)

    def AgregarNota (self , n , m):

        for item in self.ListaMaterias:
            print(item.Nombre)
            if item.nombre == m:
                item.AgregarNota (n)
                break
        for item in self.ListaMaterias:
            print(item.nombre)
            print (item.ListaDeNotas)

    #def PromedioNotasMateria (self , m):

    #   for item in self.ListaMaterias:
    #       if item.nombre == m:
    #            print (item.ListaDeNotas)
    #            return sum (item.ListaDeNotas) / len (item.ListaDeNotas)


    #def PromedioNotasAlumno(self):

    #   TotalNotas = 0;
    #    TotalCantidadNotas = 0;

    #    for item in self.ListaMaterias:
    #        TotalNotas += sum (item.ListaDeNotas)
    #        TotalCantidadNotas += len (item.ListaDeNotas)

    #    return TotalNotas / TotalCantidadNotas

    #def MayorPromedio (self):

    def MenorPromedio(self):



        #ESTA MAL, PORQUE ESTAS PASANDO COMPORTAMIENTO DE LA CLASE MATERIA A LA CLASE ALUMNO.



        #PeorPromedio = 1000;

        #for item in self.ListaMaterias:
        #    if sum(item.ListaDeNotas) / len(item.ListaDeNotas) < PeorPromedio:
        #        MenorPromedio = sum(item.ListaDeNotas) / len(item.ListaDeNotas)

        #return PeorPromedio

        #DEBERIA SER ASI:

        lista [];
        for item in self.ListaMaterias
        #no tengo ganas de escribirlo



        #una manera compacta, como deberia ser:

        return min([item.promedio for item in self.listaMaterias])


        #    MejorPromedio = 0;

        #   for item in self.ListaMaterias:
        #        if sum(item.ListaDeNotas) / len(item.ListaDeNotas) > MejorPromedio:
        #            MejorPromedio = sum(item.ListaDeNotas) / len(item.ListaDeNotas)

        #    return MejorPromedio