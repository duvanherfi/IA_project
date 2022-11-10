from Nodo import Nodo, np
from interfaz import Interfaz
#import pdb; pdb.set_trace()

costo_paso = 1
costo_estrella = 0.5
costo_koopa = 5
duracion_estrella = 6
cantidad_flor = 1

entorno = np.loadtxt('entorno.txt', dtype=int)
nodo = Nodo(entorno)
meta = np.where(entorno == 6)
meta = np.array([meta[0][0], meta[1][0]])

result = []


def ver_solucion(nodo):
    result.append(nodo.entorno)
    padre = nodo.padre
    if padre is None:
        return result
    else:
        return ver_solucion(padre)

# Búsqueda por costo uniforme, evitando devolverse


def avara(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        #breakpoint()
        # Obtener el index del nodo con costo acumulado mas bajo
        heuristica_nodos = [nodo.heuristica(goal) for nodo in stack]
        index_min_heurisitca_nodo = heuristica_nodos.index(min(heuristica_nodos))

        nodo_expandido = stack.pop(index_min_heurisitca_nodo)
        print(nodo_expandido.entorno)
        print(nodo_expandido.heuristica(goal))
        print('-----------------------------')
        ruta.append(nodo_expandido.entorno)
        # Comprobar si mario esta en la posición de la princesa
        if (np.array_equal(nodo_expandido.posm(), goal)):
            print("Se encontró a la princesa")
            return ver_solucion(nodo_expandido)
        else:
            # Izquierda
            posIzquierda = nodo_expandido.posm()[1]-1
            if (posIzquierda >= 0):
                usarOperadores(nodo_expandido.entorno[nodo_expandido.posm()[
                    0]][posIzquierda], nodo_expandido, 1, stack, arbol)

            # Derecha
            posDerecha = nodo_expandido.posm()[1]+1
            if (posDerecha <= len(nodo_expandido.entorno[0])-1):
                usarOperadores(
                    nodo_expandido.entorno[nodo_expandido.posm()[0]][posDerecha],
                    nodo_expandido, 2, stack, arbol
                )

            # Arriba
            posArriba = nodo_expandido.posm()[0]-1
            if(posArriba >= 0):
                usarOperadores(
                    nodo_expandido.entorno[posArriba][nodo_expandido.posm()[1]],
                    nodo_expandido, 3, stack, arbol
                )

            # Abajo
            posAbajo = nodo_expandido.posm()[0]+1
            if (posAbajo <= len(nodo_expandido.entorno)-1):
                usarOperadores(
                    nodo_expandido.entorno[posAbajo][nodo_expandido.posm()[1]],
                    nodo_expandido, 4, stack, arbol
                )

def usarOperadores(posicion, nodo_expandido, mover, stack, arbol):
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

        hijo = Nodo(nodo_expandido.mover(mover, nodo_expandido.pisando), nodo_expandido,
                    _costo_paso, _duracion_estrella, _cantidad_flor, _pisando)

        if not (nodo_expandido.padre != None and np.array_equal(nodo_expandido.padre.entorno, hijo.entorno)):
            stack.append(hijo)
            arbol.append(hijo)

res = avara(nodo, meta)

# Imprimir los nodos expandidos contenidos en la ruta
for entorno in res:
    print(entorno)
    print('----')

res.reverse()

Interfaz(pasos=res).show_window()
