from asyncore import close_all
from Nodo import Nodo
import numpy as np
entorno = [[1, 2, 0],[0,0,6]]
nodo = Nodo(entorno)
meta = [1, 2]

# Evitar ciclos
def evitar_ciclos(n, arrn):
    res = 0
    for elemento in arrn:
        if (np.array_equal(n,elemento)):
            res = 1
            return res
    return res

#Búsqueda por profundidad, evitando ciclos
def bfs(nodo, goal):
    stack = []
    arbol = []
    stack.append(nodo)
    arbol.append(nodo)
    ruta = []
    while len(stack) > 0:
        nodo_expandido = stack.pop(0)
        ruta.append(nodo_expandido.entorno)
        pila_index = 0
        if (nodo_expandido.posm() == goal):
            print("Se encontró a la princesa")
            return ruta
        else:
            #Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]-1] != 1):
                    hijo=Nodo(nodo_expandido.mover(1), nodo_expandido.entorno)
                    #evitar ciclo
                    if evitar_ciclos(hijo.entorno,ruta) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Derecha  
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]+1] != 1):
                    hijo=Nodo(nodo_expandido.mover(2), nodo_expandido.entorno)
                    #evitar ciclo
                    if evitar_ciclos(hijo.entorno,ruta) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Arriba  
            if(nodo_expandido.posm()[0]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]-1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(3), nodo_expandido.entorno)
                   #evitar ciclo
                    if evitar_ciclos(hijo.entorno,ruta) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Abajo  
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]+1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(4), nodo_expandido.entorno)
                    #evitar ciclo
                    if evitar_ciclos(hijo.entorno,ruta) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1 
                        arbol.append(hijo)    
                        
res = bfs(nodo, meta)

#Imprmir los nodos expandidos contenidos en la ruta
for i in res:
    print(i)

