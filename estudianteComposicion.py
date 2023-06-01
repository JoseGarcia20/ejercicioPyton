from carrera import carrera
from notas import notas 

class estudiante():
    def __init__(self, nombre, edad, carrera, notas):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = notas
        self.cursosMatriculados = []
    
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
        print("-----------------------------------------------------")
        print("Cursos Maticulados:")
        for curso in self.cursosMatriculados:
            print(f"+ {curso}")
        print("")
    
    def calcularNotaDefinitiva(self):
        
        for materia in self.carrera.pensum:
            for nota in self.notas:
                if materia == nota.nombreMateria:
                    definitiva = sum(nota.notas) / len(nota.notas)
                    print(f"La definitiva de {materia} es: {definitiva:.2f}")
    

pensum = ["Programación Java", "Estructura Datos", "Calculo"]
notasEs = [("Programación Java",[4.5, 3.7, 4.0, 4.2]),("Calculo",[2, 3, 4, 5]),("Estructura Datos",[3.5, 3.8, 4.1, 4.4])]
carrera = carrera("Ingeniería de Sistemas", 10, pensum)
notas = [notas(nota[0], nota[1]) for nota in notasEs]


estudiante = estudiante("Jose Garcia", 23, carrera, notas)
estudiante.matricularCursos("Programación Java")
estudiante.matricularCursos("Estructura Datos")
estudiante.matricularCursos("Calculo")
#Verificar que no se registra
estudiante.matricularCursos("Física")
estudiante.mostrarInformacion()
estudiante.calcularNotaDefinitiva()

