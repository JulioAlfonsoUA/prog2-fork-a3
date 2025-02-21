class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre:str, codigo:str, descripcion:str):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        type(self).total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def __str__(self) -> str:
        
        return f'{self.codigo} {self.nombre}: {self.descripcion}.'
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(nombre = "{self.nombre}", codigo = "{self.codigo}", descripcion = "{self.descripcion}")'
    
    def mostrar_detalles(self) -> str:

        return self.descripcion
    
    @classmethod

    def desde_tupla(cls,datos:tuple) -> object:

        return cls(datos[0],datos[1],datos[2])
    
    @staticmethod

    def es_curso_abierto(nombre) -> str:

        return f'El curso {nombre} esta abierto para el publico.'
