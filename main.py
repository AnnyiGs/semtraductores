from io import open
from lexico.analisisLexico2 import analizador
from sintactico.analisisSintactico import sintactico
from lexico.analisisLexico import AnalisisLexico
from utils.colores import HEADER, RESET

analizador = sintactico()

file = open("test.txt")  # cambiar el nombre del archivo de prueba
test = file.read()


print(f"\n{HEADER}--------------- CÓDIGO ---------------{RESET}\n\n{test}")


lexicoAux = AnalisisLexico(test)
lexicoAux = lexicoAux.rstrip(lexicoAux[-1])
analizador.compilador(lexicoAux)


# test  -> archivo correcto
# test2 -> provoca errores semánticos
# test3 -> ejemplo alternativo sin errores