import pytest
from estudianteHerencia import Carrera, Notas, Estudiante

#Prueba para ver si matricula una materia que esta en el pensum
def test_matricularCursoExistente():
    carreraE = Carrera("Ingeniería de Sistemas", 10, ["Programación", "Base de datos", "Redes"])
    notasE = [("Programación", [4.5, 3.7, 4.0, 4.2])]
    estudianteE = Estudiante("Jose Pere", 20, carreraE, notasE)

    estudianteE.matricular_curso("Programación")

    assert "Programación" in estudianteE.cursos_matriculados


#Prueba para determinar si matricula una materia que no esta en el pensum
def test_matricularCursoNoExistente():
    carreraE = Carrera("Ingeniería de Sistemas", 10, ["Programación", "Base de datos", "Redes"])
    notasE = [("Programación", [4.5, 3.7, 4.0, 4.2])]
    estudianteE = Estudiante("Jose Pere", 20, carreraE, notasE)

    estudianteE.matricular_curso("Algoritmos")

    assert "Algoritmos" not in estudianteE.cursos_matriculados
    
    
#Prueba para determnar si calcula de forma crrecta la definitiva
def test_calcularDefinitiva():
    carreraE = Carrera("Ingeniería de Sistemas", 10, ["Programación", "Base de datos", "Redes"])
    notasE = [Notas("Programación", [4.5, 3.7, 4.0, 4.2]), Notas("Base de datos", [3.5, 3.8, 4.1, 4.3])]
    estudianteE = Estudiante("Jose Pere", 20, carreraE, notasE)

    estudianteE.matricular_curso("Programación")
    estudianteE.matricular_curso("Base de datos")

    resultado = estudianteE.calcular_definitiva("Programación")
    
    assert resultado == 4.1


#Prueba para verificar la salida de informacion
def test_mostrarInformacion(capfd):
    carreraE = Carrera("Ingeniería de Sistemas", 10, ["Programación", "Base de datos", "Redes"])
    notasE = [("Programación", [4.5, 3.7, 4.0, 4.2]), ("Base de datos", [3.5, 3.8, 4.1, 4.3])]
    estudianteE = Estudiante("Jose Pere", 20, carreraE, notasE)

    estudianteE.matricular_curso("Programación")
    estudianteE.matricular_curso("Base de datos")

    estudianteE.mostrar_informacion()

    captura = capfd.readouterr()
    salida_esperada = "Estudiante:\nNombre: Jose Pere\nEdad: 20\nCarrera: Ingeniería de Sistemas\nNúmero de semestres: 10\nCursos matriculados:\n- Programación\n- Base de datos\n"
    assert captura.out == salida_esperada