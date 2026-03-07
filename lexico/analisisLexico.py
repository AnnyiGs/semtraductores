from utils.colores import SUBHEADER, RESET


def AnalisisLexico(test):
    """Realiza un análisis léxico sencillo sobre el código fuente.

    Imprime una tabla con TOKEN / SÍMBOLO / TIPO y regresa una
    cadena con los tokens separados por espacios, que será la
    entrada para el analizador sintáctico LR.
    """
    identificador = {'a' : 'id', 
                     'b':'id', 
                     'c':'id', 
                     'x':'id', 
                     'y':'id', 
                     'z':'id'}
    identificador_key = identificador.keys()
    operadores = {'+' : 
                  'opSuma', '-' : 
                  'opSuma', '*' : 
                  'opMult', '/' : 
                  'opMult','=' : 
                  'opRelac','<':
                  'opRelac', 
                    '>':
                    'opRelac',  
                    '<=':'opRelac', 
                    '>=':'opRelac', 
                    '!=':'opIguald', 
                    '==':'opIguald',
                    '&&':'opAnd', 
                    '||':'opOr', 
                    '!':'opNot'}
    operadores_key = operadores.keys()
    puntuacion = {';': 
                  'puntYcom', 
                  '(':'abrirPar', 
                  ')':'cerrarPar', 
                  '{':'abrirLlv', 
                  '}':'cerrarLlv',
                  ',': 'coma'}
    puntuacion_keys = puntuacion.keys()
    palabras_reservadas = {'if':'Si', 
                           'while':'Mientras', 
                           'return':'retornar', 
                           'else': 'Si no', 
                           'int':'entero', 
                           'float':'real', 
                           'main':'principal'}
    palabras_reservadas_keys = palabras_reservadas.keys()

    cont = 0
    band = 0
    test = test.split("\n")
 
    cadena=""

    # Encabezado del análisis léxico en formato de tabla.
    print(f"\n{SUBHEADER}-------- ANÁLISIS LÉXICO --------{RESET}")
    encabezado = f"{'TOKEN':<12} {'SÍMBOLO':<16} {'TIPO':<5}"
    print(encabezado)
    print("-" * len(encabezado))
    for line in test:
        cont = cont + 1
        tokens = line.split(' ')

        for token in tokens:
            tipo=""
            #print(token)

            if token in operadores_key:
                if(token=='+' or token=='-'):
                    tipo="5"
                elif(token=='*' or token=='/'):
                    tipo="6"
                elif(token=='<' or token=='<=' or token=='>' or token=='>='):
                    tipo="7"
                elif(token=='||'):
                    tipo="8"
                elif(token=='&&'):
                    tipo="9"
                elif(token=='!'):
                    tipo="10"
                elif(token=='='):
                    tipo="18"
                cadena = cadena + token + " "
                print(f"{token:<12} {operadores[token]:<16} {tipo:<5}")

            elif token in identificador_key:
                tipo="0"
                cadena = cadena + token + " "
                print(f"{token:<12} {'identificador':<16} {tipo:<5}")

            elif token in puntuacion_keys:
                if(token==';'):
                    tipo="12"
                elif(token==','):
                    tipo="13"
                if(token=='('):
                    tipo="14"
                elif(token==')'):
                    tipo="15"
                if(token=='{'):
                    tipo="16"
                elif(token=='}'):
                    tipo="17"
                cadena = cadena + token + " "
                print(f"{token:<12} {puntuacion[token]:<16} {tipo:<5}")

            elif token in palabras_reservadas_keys:
                if(token=='if'):
                    tipo="19"
                elif(token=='while'):
                    tipo="20"
                if(token=='return'):
                    tipo="21"
                elif(token=='main'):
                    tipo="0"
                if(token=='int'):
                    tipo="4"
                elif(token=='float'):
                    tipo="4"
                elif(token=='print'):
                    tipo="0"
                cadena = cadena + token + " "
                print(f"{token:<12} {palabras_reservadas[token]:<16} {tipo:<5}")

            elif ''.join(token).isdigit() == True:
                tipo = "1"
                cadena = cadena + token + " "
                print(f"{token:<12} {'numEnt':<16} {tipo:<5}")

            elif token.replace('.', '', 1).isdigit() == True:
                tipo = "2"
                cadena = cadena + token + " "
                print(f"{token:<12} {'numReal':<16} {tipo:<5}")

            elif len(''.join(token))>=1:
                if ''.join(token[0])>= 'a' and ''.join(token[0])<='z': 
                    cadena = cadena + token + " "
                    print(f"{token:<12} {'Variable':<16} {'':<5}")

            elif (token==' ' or '\n'):
                pass
    return(cadena)
