class arbolSintactico:

    def __init__(self):
        self.sangriaActual = 0
    
    def imprimirArbol(self, nodo):
        for i in reversed(nodo.elementosEliminados):
            if i.id == 2:
                i.nodo.sangria = self.sangriaActual
                i.nodo.printRegla()
            else:
                i.printValor()

        lastIndex = self.ultimoNodo(nodo)
        if type(lastIndex) == int:
            nodoAux = nodo.elementosEliminados[lastIndex].nodo
            self.sangriaActual = self.sangriaActual + len(nodoAux.regla)-2
            self.imprimirArbol(nodoAux)

    def imprimirArbolGrafico(self, nodo, prefijo="", esUltimo=True):
        conector = "└── " if esUltimo else "├── "
        etiqueta = nodo.regla if nodo.regla != "" else "<raiz>"
        print(prefijo + conector + etiqueta)

        hijos = []
        for elemento in reversed(nodo.elementosEliminados):
            if elemento.id == 2:
                hijos.append(("NT", elemento.nodo))
            elif elemento.id == 1:
                hijos.append(("T", elemento.valor))

        for indice, hijo in enumerate(hijos):
            esUlt = indice == len(hijos) - 1
            nuevoPrefijo = prefijo + ("    " if esUltimo else "│   ")

            if hijo[0] == "NT":
                self.imprimirArbolGrafico(hijo[1], nuevoPrefijo, esUlt)
            else:
                conectorHijo = "└── " if esUlt else "├── "
                print(nuevoPrefijo + conectorHijo + f"'{hijo[1]}'")

    def escribirArbolGrafico(self, nodo, archivo, prefijo="", esUltimo=True):
        conector = "└── " if esUltimo else "├── "
        etiqueta = nodo.regla if nodo.regla != "" else "<raiz>"
        archivo.write(prefijo + conector + etiqueta + "\n")

        hijos = []
        for elemento in reversed(nodo.elementosEliminados):
            if elemento.id == 2:
                hijos.append(("NT", elemento.nodo))
            elif elemento.id == 1:
                hijos.append(("T", elemento.valor))

        for indice, hijo in enumerate(hijos):
            esUlt = indice == len(hijos) - 1
            nuevoPrefijo = prefijo + ("    " if esUltimo else "│   ")

            if hijo[0] == "NT":
                self.escribirArbolGrafico(hijo[1], archivo, nuevoPrefijo, esUlt)
            else:
                conectorHijo = "└── " if esUlt else "├── "
                archivo.write(nuevoPrefijo + conectorHijo + f"'{hijo[1]}'" + "\n")

    def ultimoNodo(self,nodo):
        lastIndex = 0
        if len(nodo.elementosEliminados) > 0:
            for i in range(len(nodo.elementosEliminados)):
                nodoAux = nodo.elementosEliminados[i]
                if nodoAux.id == 2 and len(nodoAux.nodo.elementosEliminados) > 0:
                    lastIndex = i
            return lastIndex
        return False        

class Nodo:

    def __init__(self):
        self.sangria = 0
        self.elementosEliminados = []
        self.regla = ""

    def printRegla(self):
        sangriaAux = ""
        for i in range(self.sangria):
            sangriaAux += " "
        print(sangriaAux + self.regla)
