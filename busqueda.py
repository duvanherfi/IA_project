from Nodo import Nodo, np
#import pdb; pdb.set_trace()

class Busqueda:
    costo_paso = 1
    costo_estrella = 0.5
    costo_koopa = 5
    duracion_estrella = 6
    cantidad_flor = 1

    def __init__(self, entorno):
        self.nodo = Nodo(entorno)
        meta = np.where(entorno == 6)
        self.meta = np.array([meta[0][0], meta[1][0]])
        self.resultado = []
        self.stack = []
        self.arbol = []
        self.pila_index = 0
        self.nodo_expandido = None

    def reset_result(self):
        self.resultado = []
        self.nodo_expandido = None

    def evitar_ciclos(self, nodo, padre):
        if padre is None:
            return 0
        elif (np.where(nodo.entorno == 2) == np.where(padre.entorno == 2)):
            return 1
        else:
            return self.evitar_ciclos(nodo, padre.padre)

    def usarOperadores(self, posicion, nodo_expandido, mover, stack, arbol, inverso=False):
        # Comprobar si no hay un muro
        #breakpoint()
        if posicion != 1:
            _duracion_estrella = nodo_expandido.estrella
            _cantidad_flor = nodo_expandido.flor
            _pisando = 0

            if nodo_expandido.estrella > 0:  # Tiene estrella
                _costo_paso = self.costo_estrella
                _duracion_estrella = nodo_expandido.estrella - 1
            # Pisa un koopa y tiene una o mas flores
            elif posicion == 5 and nodo_expandido.flor > 0:
                _costo_paso = self.costo_paso
                _cantidad_flor = nodo_expandido.flor - 1
            elif posicion == 5:  # Pisa un koopa
                _costo_paso = self.costo_paso + self.costo_koopa
                _pisando = 5
            else:
                _costo_paso = self.costo_paso

            # Pisa una estrella y tiene una o mas flores
            if posicion == 3 and nodo_expandido.flor > 0:
                _pisando = 3
            elif posicion == 3 and nodo_expandido.flor == 0:
                _duracion_estrella = _duracion_estrella + self.duracion_estrella

            # Pisa una flor y tiene estrella
            if posicion == 4 and nodo_expandido.estrella > 0:
                _pisando = 4
            elif posicion == 4 and nodo_expandido.estrella == 0:
                _cantidad_flor = _cantidad_flor + self.cantidad_flor

            hijo = Nodo(nodo_expandido.mover(mover, nodo_expandido.pisando), nodo_expandido,
                        _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

            if not (nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno)):
                if self.evitar_ciclos(hijo, nodo_expandido) != 1:
                    if inverso:
                        stack.insert(self.pila_index, hijo)
                        self.pila_index += 1
                        arbol.append(hijo)
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)

    def ver_solucion(self, nodo):
        print("***************")
        print(nodo.entorno)
        self.resultado.append(nodo.entorno)
        padre = nodo.padre
        if padre is None:
            return self.resultado
        else:
            return self.ver_solucion(padre)

    def movimientos(self, nodo_expandido, inverso=False):
        # Izquierda
        posIzquierda = nodo_expandido.posm()[1] - 1
        if (posIzquierda >= 0):
            self.usarOperadores(
                nodo_expandido.entorno[nodo_expandido.posm()[0]][posIzquierda],
                nodo_expandido, 1, self.stack, self.arbol, inverso
            )

        # Derecha
        posDerecha = nodo_expandido.posm()[1] + 1
        if (posDerecha <= len(nodo_expandido.entorno[0]) - 1):
            self.usarOperadores(
                nodo_expandido.entorno[nodo_expandido.posm()[0]][posDerecha],
                nodo_expandido, 2, self.stack, self.arbol, inverso
            )

        # Arriba
        posArriba = nodo_expandido.posm()[0] - 1
        if (posArriba >= 0):
            self.usarOperadores(
                nodo_expandido.entorno[posArriba][nodo_expandido.posm()[1]],
                nodo_expandido, 3, self.stack, self.arbol, inverso
            )

        # Abajo
        posAbajo = nodo_expandido.posm()[0] + 1
        if (posAbajo <= len(nodo_expandido.entorno) - 1):
            self.usarOperadores(
                nodo_expandido.entorno[posAbajo][nodo_expandido.posm()[1]],
                nodo_expandido, 4, self.stack, self.arbol, inverso
            )

    def avara(self):
        self.stack = []
        self.arbol = []
        self.stack.append(self.nodo)
        self.arbol.append(self.nodo)
        ruta = []
        while len(self.stack) > 0:
            # breakpoint()
            # Obtener el index del nodo con costo acumulado mas bajo
            heuristica_nodos = [nodo.heuristica(self.meta) for nodo in self.stack]
            index_min_heurisitca_nodo = heuristica_nodos.index(min(heuristica_nodos))

            self.nodo_expandido = self.stack.pop(index_min_heurisitca_nodo)
            print(self.nodo_expandido.entorno)
            print(self.nodo_expandido.heuristica(self.meta))
            print('-----------------------------')
            ruta.append(self.nodo_expandido.entorno)
            # Comprobar si mario esta en la posición de la princesa
            if (np.array_equal(self.nodo_expandido.posm(), self.meta)):
                print("Se encontró a la princesa")
                return self.ver_solucion(self.nodo_expandido)
            else:
                self.movimientos(self.nodo_expandido)

    def a_estrella(self):
        self.stack = []
        self.arbol = []
        self.stack.append(self.nodo)
        self.arbol.append(self.nodo)
        ruta = []
        while len(self.stack) > 0:
            # breakpoint()
            # Obtener el index del nodo con costo acumulado mas bajo
            heuristica_costo_nodos = [nodo.heuristica(self.meta) + nodo.costoAcumulado() for nodo in self.stack]
            index_min_heurisitca_costo_nodo = heuristica_costo_nodos.index(min(heuristica_costo_nodos))

            self.nodo_expandido = self.stack.pop(index_min_heurisitca_costo_nodo)
            print(self.nodo_expandido.entorno)
            print(self.nodo_expandido.heuristica(self.meta))
            print('-----------------------------')
            ruta.append(self.nodo_expandido.entorno)
            # Comprobar si mario esta en la posición de la princesa
            if (np.array_equal(self.nodo_expandido.posm(), self.meta)):
                print("Se encontró a la princesa")
                return self.ver_solucion(self.nodo_expandido)
            else:
                self.movimientos(self.nodo_expandido)

    def ucs(self):
        self.stack = []
        self.arbol = []
        self.stack.append(self.nodo)
        self.arbol.append(self.nodo)
        ruta = []
        while len(self.stack) > 0:
            # Obtener el index del nodo con costo acumulado mas bajo
            costoNodos = [nodo.costoAcumulado() for nodo in self.stack]
            indexMinCostoNodo = costoNodos.index(min(costoNodos))

            self.nodo_expandido = self.stack.pop(indexMinCostoNodo)
            print(self.nodo_expandido.entorno)
            print(self.nodo_expandido.costoAcumulado())
            print('-----------------------------')
            ruta.append(self.nodo_expandido.entorno)
            # Comprobar si mario esta en la posición de la princesa
            print(self.nodo_expandido.posm())
            print(self.meta)
            if (np.array_equal(self.nodo_expandido.posm(), self.meta)):
                print("Se encontró a la princesa")
                return self.ver_solucion(self.nodo_expandido)
            else:
                self.movimientos(self.nodo_expandido)

    def dfs(self):
        self.stack = []
        self.arbol = []
        self.stack.append(self.nodo)
        self.arbol.append(self.nodo)
        ruta = []
        while len(self.stack) > 0:
            self.nodo_expandido = self.stack.pop(0)
            ruta.append(self.nodo_expandido.entorno)
            self.pila_index = 0
            print(self.nodo_expandido.entorno)
            print('-----------------------------')
            ruta.append(self.nodo_expandido.entorno)
            # Comprobar si mario esta en la posición de la princesa
            print(self.nodo_expandido.posm())
            print(self.meta)
            if (np.array_equal(self.nodo_expandido.posm(), self.meta)):
                print("Se encontró a la princesa")
                return self.ver_solucion(self.nodo_expandido)
            else:
                self.movimientos(self.nodo_expandido, True)

    def bfs(self):
        self.stack = []
        self.arbol = []
        self.stack.append(self.nodo)
        self.arbol.append(self.nodo)
        ruta = []
        while len(self.stack) > 0:
            nodo_expandido = self.stack.pop(0)
            ruta.append(nodo_expandido.entorno)
            if (np.array_equal(nodo_expandido.posm(), self.meta)):
                print("Se encontró a la princesa")
                return self.ver_solucion(nodo_expandido)
            else:
                self.movimientos(nodo_expandido)
