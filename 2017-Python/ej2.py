from Clases.materia import materia
from Clases.alumno import alumno





MiAlumno = alumno ()
m=materia()
MiAlumno.ListaMaterias.append(m)
m.AgregarNota(10)
m1=materia()
MiAlumno.ListaMaterias.append(m1)
m1.AgregarNota(9)
m1=materia()
MiAlumno.ListaMaterias.append(m1)

for item1 in MiAlumno.ListaMaterias:
    print (item1.ListaDeNotas)


MiAlumno.SetNombre (input ("ingrese un nombre: "))

MiAlumno.SetApellido (input ("ingrese un apellido: "))

MiAlumno.SetFechaNacimiento (int(input ("agregue un año: ")) , int(input ("agrege un mes (numerico): ")) , int (input ("Agregue un dia (numerico): ")))


MiAlumno.AgregarMateria (input ("agregar una materia: "))
MiAlumno.AgregarMateria (input ("agregar una materia: "))
MiAlumno.AgregarMateria (input ("agregar una materia: "))

MiAlumno.AgregarNota (int (input ("agregar una nota: ")) , str (input ("¿para que materia es esa nota?: ")))
MiAlumno.AgregarNota (int (input ("agregar una nota: ")) , str (input ("¿para que materia es esa nota?: ")))
MiAlumno.AgregarNota (int (input ("agregar una nota: ")) , str (input ("¿para que materia es esa nota?: ")))

materia = input ("que materia desea saber promedio: ")

print ("el promedio de la materia " + str (materia) + " es:" + str (MiAlumno.PromedioNotasMateria (materia)))

print ("El promedio de las notas del alumno es de: " + str (MiAlumno.PromedioNotasAlumno()))

print (("el mayor promedio de entre todas las materias es de: ") + str (MiAlumno.MayorPromedio()))

print (("el menor promedio de entre todas las materias es de: ") + str (MiAlumno.MenorPromedio()))

#datetime.date (2017 , 3 , 16)