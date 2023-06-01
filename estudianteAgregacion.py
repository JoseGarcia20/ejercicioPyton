from carrera import carrera
from notas import notas 

class estudiante():
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.cursosMatriculados = []
        self.notas = []
    
    def matricularCursos(self, curso):
        if curso in self.carrera.pensum:
            self.cursosMatriculados.append(curso)
            print(f"El curso {curso} se ha matriculado correctamente.")
        else:
            print("El curso que ingresó, no se encuentra en el pensum. Verifique e intente nuevamente.")
        print("")
    
    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nombre Carrera: {self.carrera.nombreCarrera}")
        print(f"Número de semestres: {self.carrera.numSemestres}")
        print(f"Cursos matriculados: {', '.join(self.cursosMatriculados)}")
        print("")
    
    def calcularNotaDefinitiva(self):
        print(f"Las notas del estudiante {self.nombre} son:")
        for nota in self.notas:
            if nota.nombreMateria in self.cursosMatriculados:
                promedio = sum(nota.notas) / len(nota.notas)
                print(f"Materia: {nota.nombreMateria}, Definitiva: {promedio}")

    

pensum = ["Programación Java", "Estructura Datos", "Calculo"]
carrera = carrera("Ingeniería de Sistemas", 10, pensum)
notasPro = notas("Programación Java", [4.5, 3.7, 4.0, 4.2])
notasEst = notas("Estructura Datos", [2, 3, 4, 5])
notasCal = notas("Calculo", [3.5, 3.8, 4.1, 4.4])

estudiante = estudiante("Jose Garcia", 23, carrera)
estudiante.matricularCursos("Programación Java")
estudiante.matricularCursos("Estructura Datos")
estudiante.matricularCursos("Calculo")
#Verificar que no se registra
estudiante.matricularCursos("Física")
estudiante.mostrarInformacion()

estudiante.notas = [notasCal, notasEst, notasPro]
estudiante.calcularNotaDefinitiva()

