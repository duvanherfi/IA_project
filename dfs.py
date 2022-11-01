from Nodo import Nodo
import numpy as np
entorno = [[1, 2, 0],[0,0,6]]
nodo = Nodo(entorno)
meta = [1, 2]

# Evitar ciclos 
def evitar_ciclos(nodo,padre):
    if padre is None:
        return 0
    elif (np.array_equal(nodo.entorno,padre.entorno)):
        return 1
    else:
     return evitar_ciclos(nodo,padre.padre)

#Imprimir solución
res = []
def ver_solucion(nodo):
    res.append(nodo.entorno)
    padre = nodo.padre
    if padre is None:
        return res
    else:
        return ver_solucion(padre)

#Búsqueda por profundidad, evitando ciclos
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
        if (nodo_expandido.posm() == goal):
            print("Se encontró a la princesa")
            return ver_solucion(nodo_expandido)
        else:
            #Izquierda
            if (nodo_expandido.posm()[1]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]-1] != 1):
                    hijo=Nodo(nodo_expandido.mover(1), nodo_expandido)
                    #evitar ciclo
                    if evitar_ciclos(hijo, hijo.padre) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Derecha  
            if (nodo_expandido.posm()[1]+1 <= len(nodo_expandido.entorno[0])-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]][nodo_expandido.posm()[1]+1] != 1):
                    hijo=Nodo(nodo_expandido.mover(2), nodo_expandido)
                    #evitar ciclo
                    if evitar_ciclos(hijo, hijo.padre) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Arriba  
            if(nodo_expandido.posm()[0]-1 >= 0):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]-1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(3), nodo_expandido)
                   #evitar ciclo
                    if evitar_ciclos(hijo, hijo.padre) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1
                        arbol.append(hijo)
            #Abajo  
            if (nodo_expandido.posm()[0]+1 <= len(nodo_expandido.entorno)-1):
                # Comprobar si hay un muro
                if(nodo_expandido.entorno[nodo_expandido.posm()[0]+1][nodo_expandido.posm()[1]] != 1):
                    hijo=Nodo(nodo_expandido.mover(4), nodo_expandido)
                    #evitar ciclo
                    if evitar_ciclos(hijo,hijo.padre) == 1:
                        pass    
                    else:
                        stack.insert(pila_index,hijo)
                        pila_index += 1 
                        arbol.append(hijo)    
                        
print(dfs(nodo,meta))

