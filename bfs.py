from Nodo import Nodo, np
from interfaz import Interfaz
entorno = np.loadtxt('entorno.txt', dtype=int)
nodo = Nodo(entorno)
meta = np.where(entorno == 6)
meta = np.array([meta[0][0], meta[1][0]])

res = []


def ver_solucion(nodo):
    res.append(nodo.entorno)
    padre = nodo.padre
    if padre is None:
        return res
    else:
        return ver_solucion(padre)

# Búsqueda por amplitud, evitando devolverse


def bfs(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        nodo_expandido = stack.pop(0)
        ruta.append(nodo_expandido.entorno)
        if (np.array_equal(nodo_expandido.posm(), goal)):
            print("Se encontró a la princesa")
            return ver_solucion(nodo_expandido)
        else:
            # Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                _posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]-1]
                # Comprobar si hay un muro
                if(_posicion != 1):
                    _pisando =0
                    if (_posicion == 5):
                        _pisando = 5
                    elif (_posicion == 3):
                        _pisando = 3
                    elif (_posicion == 4):
                        _pisando = 4
                    hijo = Nodo(nodo_expandido.mover(1, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar devolverse
                    if nodo_expandido.padre != None and np.where(hijo.entorno ==2) == np.where(nodo_expandido.padre.entorno ==2):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Derecha
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                _posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]+1]
                # Comprobar si hay un muro
                if(_posicion != 1):
                    _pisando =0
                    if (_posicion == 5):
                        _pisando = 5
                    elif (_posicion == 3):
                        _pisando = 3
                    elif (_posicion == 4):
                        _pisando = 4
                    hijo = Nodo(nodo_expandido.mover(2, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar devolverse
                    if nodo_expandido.padre != None and np.where(hijo.entorno ==2) == np.where(nodo_expandido.padre.entorno ==2):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Arriba
            if(nodo_expandido.posm()[0]-1 >= 0):
                _posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]-1][nodo_expandido.posm()[1]]

                # Comprobar si hay un muro
                if(_posicion != 1):
                    _pisando =0
                    if (_posicion == 5):
                        _pisando = 5
                    elif (_posicion == 3):
                        _pisando = 3
                    elif (_posicion == 4):
                        _pisando = 4
                    hijo = Nodo(nodo_expandido.mover(3, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar devolverse
                    if nodo_expandido.padre != None and np.where(hijo.entorno ==2) == np.where(nodo_expandido.padre.entorno ==2):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)
            # Abajo
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                _posicion = nodo_expandido.entorno[nodo_expandido.posm()[0]+1][nodo_expandido.posm()[1]]
                # Comprobar si hay un muro
                if(_posicion != 1):
                    _pisando =0
                    if (_posicion == 5):
                        _pisando = 5
                    elif (_posicion == 3):
                        _pisando = 3
                    elif (_posicion == 4):
                        _pisando = 4
                    hijo = Nodo(nodo_expandido.mover(4, nodo_expandido.pisando),nodo_expandido,pisando=_pisando)
                    # evitar devolverse
                    if nodo_expandido.padre != None and np.where(hijo.entorno ==2) == np.where(nodo_expandido.padre.entorno ==2):
                        pass
                    else:
                        stack.append(hijo)
                        arbol.append(hijo)


res = bfs(nodo, meta)

# Imprmir los nodos expandidos contenidos en la ruta
for entorno in res:
    print(entorno)
    print('----')

res.reverse()

Interfaz(pasos=res).show_window()
