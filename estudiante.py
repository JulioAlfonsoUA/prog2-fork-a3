class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre : str, edad : int, cursos_inscritos : list[str]) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        type(self).total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante

    def inscribir_curso(self, curso : str) -> None:
        """
        Añade un nuevo curso a la lista de cursos en los que
        está inscrito el estudiante
        :param curso: nombre del curso
        :return: nada
        """

        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)

    def mostrar_informacion(self) -> None:
        print(f'Cursos en los que está inscrito el estudiante "{self.nombre}" de "{self.edad}" años\n')

        for i,curso in enumerate(self.cursos_inscritos):
            print(f'Curso {i+1} -> {curso}')


    def __str__(self) -> str:
        return (f'Nombre: "{self.nombre}", de edad: "{self.edad}" e inscrito en los curos: "{self.cursos_inscritos}"')

    def __repr__(self) -> str:
        return (f'"{type(self).__name__}" (Nombre -> "{self.nombre}", edad ->  "{self.edad}", curos -> "{self.cursos_inscritos}")')

    @classmethod
    def desde_tupla(cls,tupla : tuple) -> None:
        return cls(tupla[0], tupla[1], tupla[2])

    @staticmethod
    def es_mayor_de(edad : int) -> None:
        if edad >= 17:
            print('Es mayor de edad\n')
        else:
            print('No es mayor de edad')


Jorge = Estudiante('Julio',18,['Programacion','Mates'])
Julio = Estudiante('Julio',18,['Programacion','Física'])
print(Estudiante.total_estudiantes)
print(Julio)
print()
print(repr(Jorge))
Julio.es_mayor_de(Julio.edad)
Jorge.mostrar_informacion()
Julio.inscribir_curso('Mates')
Julio.mostrar_informacion()
