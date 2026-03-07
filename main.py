from io import open
import elementoPila
from analisisLexico2 import analizador
from pila import stack
from analisisSintactico import sintactico
from analisisLexico import *
from colores import HEADER, RESET

analizador = sintactico()
file = open("test.txt")
test = file.read()
print(f"\n{HEADER}---------- EJEMPLO DE CÓDIGO ----------{RESET}\n\n{test}")
lexicoAux = AnalisisLexico(test)
lexicoAux = lexicoAux.rstrip(lexicoAux[-1])
analizador.compilador(lexicoAux)



#test archivo correcto
#test2 da errores 
#test3 es una prueba que no da error pero es interesante