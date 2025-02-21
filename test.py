class Usuario:

    def __init__(self, nombre : str, edad : int):
        self.nombre = nombre
        self.edad = edad
        self.inscrito = True

    def __str__(self) -> str:
        return f"Usuario de nombre {self.nombre} de {self.edad} años"

Carlitos = Usuario("Carlitos", 20)
print(Carlitos)