#IMPORTS
from email import generator
from errno import ESTALE
from Romance import Romance
from Academico import Academico

#SISTEMA
romance1 = Romance("Titulo 1", "Autor 1", 259, 56.90, "Fantasia")
# print(romance1)

academico1 = Academico("JavaScript: O Guia Definitivo", "David Flanagan", 400, 250.00, "TI")
academico2 = Academico("Academico 2", "Noe", 210, 200.00, "Enfermagem")
# print(academico1)

# print(academico1 > romance1)

lista = [romance1,academico1]

for livro in lista:
    if isinstance(livro,Romance):
        print(livro)

print("\n------------------------\n")

for livro in lista:
    if isinstance(livro,Academico):
        print(livro)