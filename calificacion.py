class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def aprob(self):
        return self.calificacion >= 60


est = Estudiante("Jorge", 24, 82)
est2 = Estudiante("Karina", 35, 50)

print(f"{est.nombre} ha aprobado: {est.aprob()}")
print(f"{est2.nombre} ha aprobado: {est2.aprob()}")
