from Nodo import Nodo
import numpy as np
from interfaz import Interfaz

costo_paso = 1
costo_estrella = 0.5
costo_koopa = 5
duracion_estrella = 6
cantidad_flor = 1

entorno = np.loadtxt('entorno.txt', dtype=int)
nodo = Nodo(entorno)
meta = np.where(entorno == 6)
meta = [meta[0], meta[1]]

result = []


def ver_solucion(nodo):
    result.append(nodo.entorno)
    padre = nodo.padre
    if padre is None:
        return result
    else:
        return ver_solucion(padre)

# Búsqueda por costo uniforme, evitando devolverse


def ucs(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        # Obtener el index del nodo con costo acumulado mas bajo
        costoNodos = [nodo.costoAcumulado() for nodo in stack]
        indexMinCostoNodo = costoNodos.index(min(costoNodos))
        # print(costoNodos)

        nodo_expandido = stack.pop(indexMinCostoNodo)
        print(nodo_expandido.entorno)
        print(nodo_expandido.costoAcumulado())
        print('-----------------------------')
        ruta.append(nodo_expandido.entorno)
        # Comprobar si mario esta en la posición de la princesa
        if (nodo_expandido.posm() == goal):
            # print("Se encontró a la princesa")
            return ver_solucion(nodo_expandido)
        else:
            # Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[
                    0]][nodo_expandido.posm()[1]-1]
                # Comprobar si no hay un muro
                if(posicion != 1):
                    _duracion_estrella = nodo_expandido.estrella
                    _cantidad_flor = nodo_expandido.flor
                    _pisando = 0

                    if (nodo_expandido.estrella > 0):  # Tiene estrella
                        _costo_paso = costo_estrella
                        _duracion_estrella = nodo_expandido.estrella - 1
                    # Pisa un koopa y tiene una o mas flores
                    elif (posicion == 5 and nodo_expandido.flor > 0):
                        _costo_paso = costo_paso
                        _cantidad_flor = nodo_expandido.flor - 1
                    elif (posicion == 5):  # Pisa un koopa
                        _costo_paso = costo_paso + costo_koopa
                        _pisando = 5
                    else:
                        _costo_paso = costo_paso

                    # Pisa una estrella y tiene una o mas flores
                    if (posicion == 3 and nodo_expandido.flor > 0):
                        _pisando = 3
                    elif (posicion == 3 and nodo_expandido.flor == 0):
                        _duracion_estrella = _duracion_estrella + duracion_estrella

                    # Pisa una flor y tiene estrella
                    if (posicion == 4 and nodo_expandido.estrella > 0):
                        _pisando = 4
                    elif (posicion == 4 and nodo_expandido.estrella == 0):
                        _cantidad_flor = _cantidad_flor + cantidad_flor

                    hijo = Nodo(nodo_expandido.mover(1, nodo_expandido.pisando), nodo_expandido,
                                _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

                    if nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Derecha
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[
                    0]][nodo_expandido.posm()[1]+1]
                # Comprobar si no hay un muro
                if(posicion != 1):
                    _duracion_estrella = nodo_expandido.estrella
                    _cantidad_flor = nodo_expandido.flor
                    _pisando = 0

                    if (nodo_expandido.estrella > 0):  # Tiene estrella
                        _costo_paso = costo_estrella
                        _duracion_estrella = nodo_expandido.estrella - 1
                    # Pisa un koopa y tiene una o mas flores
                    elif (posicion == 5 and nodo_expandido.flor > 0):
                        _costo_paso = costo_paso
                        _cantidad_flor = nodo_expandido.flor - 1
                    elif (posicion == 5):  # Pisa un koopa
                        _costo_paso = costo_paso + costo_koopa
                        _pisando = 5
                    else:
                        _costo_paso = costo_paso

                    # Pisa una estrella y tiene una o mas flores
                    if (posicion == 3 and nodo_expandido.flor > 0):
                        _pisando = 3
                    elif (posicion == 3 and nodo_expandido.flor == 0):
                        _duracion_estrella = _duracion_estrella + duracion_estrella

                    # Pisa una flor y tiene estrella
                    if (posicion == 4 and nodo_expandido.estrella > 0):
                        _pisando = 4
                    elif (posicion == 4 and nodo_expandido.estrella == 0):
                        _cantidad_flor = _cantidad_flor + cantidad_flor

                    hijo = Nodo(nodo_expandido.mover(2, nodo_expandido.pisando), nodo_expandido,
                                _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

                    if nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Arriba
            if(nodo_expandido.posm()[0]-1 >= 0):
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[
                    0]-1][nodo_expandido.posm()[1]]
                # Comprobar si no hay un muro
                if(posicion != 1):
                    _duracion_estrella = nodo_expandido.estrella
                    _cantidad_flor = nodo_expandido.flor
                    _pisando = 0

                    if (nodo_expandido.estrella > 0):  # Tiene estrella
                        _costo_paso = costo_estrella
                        _duracion_estrella = nodo_expandido.estrella - 1
                    # Pisa un koopa y tiene una o mas flores
                    elif (posicion == 5 and nodo_expandido.flor > 0):
                        _costo_paso = costo_paso
                        _cantidad_flor = nodo_expandido.flor - 1
                    elif (posicion == 5):  # Pisa un koopa
                        _costo_paso = costo_paso + costo_koopa
                        _pisando = 5
                    else:
                        _costo_paso = costo_paso

                    # Pisa una estrella y tiene una o mas flores
                    if (posicion == 3 and nodo_expandido.flor > 0):
                        _pisando = 3
                    elif (posicion == 3 and nodo_expandido.flor == 0):
                        _duracion_estrella = _duracion_estrella + duracion_estrella

                    # Pisa una flor y tiene estrella
                    if (posicion == 4 and nodo_expandido.estrella > 0):
                        _pisando = 4
                    elif (posicion == 4 and nodo_expandido.estrella == 0):
                        _cantidad_flor = _cantidad_flor + cantidad_flor

                    hijo = Nodo(nodo_expandido.mover(3, nodo_expandido.pisando), nodo_expandido,
                                _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

                    if nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Abajo
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[
                    0]+1][nodo_expandido.posm()[1]]
                # Comprobar si no hay un muro
                if(posicion != 1):
                    _duracion_estrella = nodo_expandido.estrella
                    _cantidad_flor = nodo_expandido.flor
                    _pisando = 0

                    if (nodo_expandido.estrella > 0):  # Tiene estrella
                        _costo_paso = costo_estrella
                        _duracion_estrella = nodo_expandido.estrella - 1
                    # Pisa un koopa y tiene una o mas flores
                    elif (posicion == 5 and nodo_expandido.flor > 0):
                        _costo_paso = costo_paso
                        _cantidad_flor = nodo_expandido.flor - 1
                    elif (posicion == 5):  # Pisa un koopa
                        _costo_paso = costo_paso + costo_koopa
                        _pisando = 5
                    else:
                        _costo_paso = costo_paso

                    # Pisa una estrella y tiene una o mas flores
                    if (posicion == 3 and nodo_expandido.flor > 0):
                        _pisando = 3
                    elif (posicion == 3 and nodo_expandido.flor == 0):
                        _duracion_estrella = _duracion_estrella + duracion_estrella

                    # Pisa una flor y tiene estrella
                    if (posicion == 4 and nodo_expandido.estrella > 0):
                        _pisando = 4
                    elif (posicion == 4 and nodo_expandido.estrella == 0):
                        _cantidad_flor = _cantidad_flor + cantidad_flor

                    hijo = Nodo(nodo_expandido.mover(4, nodo_expandido.pisando), nodo_expandido,
                                _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

                    if nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)


res = ucs(nodo, meta)

# Imprimir los nodos expandidos contenidos en la ruta
for entorno in res:
    print(entorno)
    print('----')

res.reverse()

Interfaz(pasos=res).show_window()
