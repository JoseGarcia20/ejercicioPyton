class Carrera:
    def __init__(self, nomcarrera, semestres, pensum):
        self.nomcarrera = nomcarrera
        self.semestres = semestres
        self.pensum = pensum

    def __str__(self):
        return f"Carrera: {self.nomcarrera}\nSemestres: {self.semestres}\nPensum: {', '.join(self.pensum)}\n"


class Notas:
    def __init__(self, nommateria, notas):
        self.nommateria = nommateria
        self.notas = notas

    def __str__(self):
        return f"Materia: {self.nommateria}\nNotas: {', '.join(str(nota) for nota in self.notas)}\n"


class Estudiante(Carrera, Notas):
    def __init__(self, nombre, edad, carrera, notas):
        self.nombre = nombre
        self.edad = edad
        Carrera.__init__(self, carrera.nomcarrera, carrera.semestres, carrera.pensum)
        self.Notas = [Notas(nota[0], nota[1]) for nota in Notas]
        self.cursos_matriculados = []

    def matricular_curso(self, curso):
        if curso in self.pensum:
            self.cursos_matriculados.append(curso)
            print(f"El curso {curso} ha sido matriculado con éxito.\n")
        else:
            print(f"El curso {curso} no está en el pensum de la carrera.\n")

    def mostrar_informacion(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.nomcarrera}")
        print(f"Número de semestres: {self.semestres}")
        print("Cursos matriculados:")
        for curso in self.cursos_matriculados:
            print(f"- {curso}")

    def calcular_definitiva(self):
        for materia in self.cursos_matriculados:
            for nota in self.notas:
                if materia == nota.nommateria:
                    definitiva = sum(nota.notas) / len(nota.notas)
                    print(f"Definitiva de {materia}: {definitiva:.2f}")

    def __str__(self):
        cursos_matriculados = "\n".join(f"- {curso}" for curso in self.cursos_matriculados)
        return f"Información del estudiante:\nNombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.nomcarrera}\nCursos matriculados:\n{cursos_matriculados}\n"


pensum = ["Programación Java", "Estructura de datos", "Redes"]
notasEst = [("Programación Java", [4.5, 3.7, 4.0, 4.2]), ("Estructura de datos", [2, 3, 4, 5])]

carrera = Carrera("Ingeniería de Sistemas", 10, pensum)
notas = notasEst

estudiante = Estudiante("Jose Garcia", 20, carrera, notas)
estudiante.matricular_curso("Programación")
estudiante.matricular_curso("Redes")
print(estudiante)
estudiante.calcular_definitiva()
