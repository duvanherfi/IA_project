from Node import Node
import numpy as np
entorno = [[0, 3, 0],[0,0,2]]
nodo = Node(entorno)
goal = [1, 2]
def val(n, arrn):
    res = 0
    for element in arrn:
        if (np.array_equal(n,element)):
            res = 1
            return res
    return res

def bfs(node, goal):
    stack = []
    stack.append(node)
    rute = []
    while len(stack) > 0:
        nodo = stack.pop(0)
        rute.append(nodo.entorno)
        if (nodo.posm() == goal):
            print("Se encontró a la princesa")
            return rute
        else:
            if (nodo.posm()[1]-1 >= 0):
                hijo=Node(nodo.mover(1))
                if val(hijo.entorno, rute)!=1:
                    stack.append(hijo)
                else:
                    pass    
                
            if (nodo.posm()[1]+1 <= len(nodo.entorno[0])-1):
                hijo=Node(nodo.mover(2))
                if  val(hijo.entorno, rute)!=1:
                    stack.append(hijo)
                else:
                    pass    
                
            if(nodo.posm()[0]-1 >= 0):
                hijo=Node(nodo.mover(3))
                if  val(hijo.entorno, rute)!=1:
                    stack.append(hijo)
                else:
                    pass    
                
            if (nodo.posm()[0]+1 <= len(nodo.entorno)-1):
                hijo=Node(nodo.mover(4))
                if  val(hijo.entorno, rute)!=1:
                    stack.append(hijo)
                else:
                    pass              
    return rute


res = bfs(nodo, goal)

for i in res:
    print(i)

