class Persona:
    def __init__(self, nombre, edad): #Constructor
        self.nombre = nombre
        self.edad = edad

import pandas as pd
p1 = Persona("Juan",14)

print(p1.nombre)
print(p1.edad)


myList = ["a","b","c"]
myNewList = pd.Series(myList, index=[1,2,3])
print(pd.Series(myNewList))
print(pd.DataFrame(myNewList))