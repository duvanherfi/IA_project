from Nodo import Nodo, np
from interfaz import Interfaz

entorno = np.loadtxt('entorno.txt', dtype=int)
nodo = Nodo(entorno)
meta = np.where(entorno == 6)
meta = np.array([meta[0][0], meta[1][0]])

# Evitar ciclos
def evitar_ciclos(nodo, padre):
    if padre is None:
        return 0
    elif (np.where(nodo.entorno ==2) == np.where(padre.entorno ==2)):
        return 1
    else:
        return evitar_ciclos(nodo, padre.padre)

# Imprimir solución
res = []


def ver_solucion(nodo):
    res.append(nodo.entorno)
    padre = nodo.padre
    if padre is None:
        return res
    else:
        return ver_solucion(padre)

# Búsqueda por profundidad, evitando ciclos


def dfs(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        nodo_expandido = stack.pop(0)
        ruta.append(nodo_expandido.entorno)
        pila_index = 0
        if (np.array_equal(nodo_expandido.posm(), goal)):
            print("Se encontró a la princesa")
            return ver_solucion(nodo_expandido)
        else:
            # Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]-1]
                # Comprobar si hay un muro
                if(posicion != 1):
                    _pisando =0
                    if (posicion == 5):
                        _pisando = 5
                    elif (posicion == 3):
                        _pisando = 3
                    elif (posicion == 4):
                        _pisando == 4
                    hijo = Nodo(nodo_expandido.mover(1, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar ciclo
                    if evitar_ciclos(hijo, nodo_expandido) != 1:
                        stack.insert(pila_index, hijo)
                        pila_index += 1
                        arbol.append(hijo)
                   
            # Derecha
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                # Comprobar si hay un muro
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]+1]
                # Comprobar si hay un muro
                if(posicion != 1):
                    _pisando =0
                    if (posicion == 5):
                        _pisando = 5
                    elif (posicion == 3):
                        _pisando = 3
                    elif (posicion == 4):
                        _pisando == 4
                    hijo = Nodo(nodo_expandido.mover(2, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar ciclo
                    if evitar_ciclos(hijo, nodo_expandido) != 1:
                        stack.insert(pila_index, hijo)
                        pila_index += 1
                        arbol.append(hijo)
                    
            # Arriba
            if(nodo_expandido.posm()[0]-1 >= 0):
                # Comprobar si hay un muro
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]-1][nodo_expandido.posm()[1]]
                # Comprobar si hay un muro
                if(posicion != 1):
                    _pisando =0
                    if (posicion == 5):
                        _pisando = 5
                    elif (posicion == 3):
                        _pisando = 3
                    elif (posicion == 4):
                        _pisando == 4
                    hijo = Nodo(nodo_expandido.mover(3, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar ciclo
                    if evitar_ciclos(hijo, nodo_expandido) != 1:
                        stack.insert(pila_index, hijo)
                        pila_index += 1
                        arbol.append(hijo)
                   
            # Abajo
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                # Comprobar si hay un muro
                posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]+1][nodo_expandido.posm()[1]]
                # Comprobar si hay un muro
                if(posicion != 1):
                    _pisando =0
                    if (posicion == 5):
                        _pisando = 5
                    elif (posicion == 3):
                        _pisando = 3
                    elif (posicion == 4):
                        _pisando == 4
                    hijo = Nodo(nodo_expandido.mover(4, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar ciclo
                    if evitar_ciclos(hijo, nodo_expandido) != 1:
                        stack.insert(pila_index, hijo)
                        pila_index += 1
                        arbol.append(hijo)
                   


res = dfs(nodo, meta)

for entorno in res:
    print(entorno)
    print('----')

res.reverse()

Interfaz(pasos=res).show_window()
