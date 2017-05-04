from Clases.ej1alumno import alumno

MiAlumno = alumno ()

MiAlumno.SetNombre (input ("ingrese un nombre: "))

MiAlumno.SetApellido (input ("ingrese un apellido: "))

MiAlumno.SetFechaNacimiento (int(input ("agregue un año: ")) , int(input ("agrege un mes (numerico): ")) , int (input ("Agregue un dia (numerico): ")))

MiAlumno.AgregarNota (int (input ("agregar una nota: ")))
MiAlumno.AgregarNota (int (input ("agregar una nota: ")))
MiAlumno.AgregarNota (int (input ("agregar una nota: ")))

print ("la menor nota es: " + str (MiAlumno.MenorNota()))

print ("la mayor nota es: " + str (MiAlumno.MayorNota()))

print ("El promedio de las notas es de: " + str (MiAlumno.PromedioNota()))

#datetime.date (2017 , 3 , 16)