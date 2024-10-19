#!/usr/bin/env python3

import copy    

n = 3

def isTerminal(state: list):

    res = (False, None)
    completa = 0
    
    d1 = sum([state[i][i] for i in range(n)])

    if d1 == n or d1 == -n:
        return (True, d1/n)

    d2 = sum([state[i][z] for i,z in zip(range(n), reversed(range(n)))])   
    
    if d2 == n or d2 == -n:
        return (True, d2/n)

    for i in range(n):

        row = state[i]
        sr = sum(row)

        sc = sum([state[x][i] for x in range(n)])
        
        completa = completa if 0 in row else completa +1 

        if sr == n or sr == -n:
            return (True, sr/n)
            

        if sc == n or sc == -n:
            return (True, sc/n)
            

    if completa == n:
        return (True, 0)
    
    return res


def childrens(state, maximizingPlayer):
    res = list()
    for i in range(len(state)):
        row = state[i]
        for e in range(len(row)):
            state2 = copy.deepcopy(state)
            if row[e] == 0:
                if maximizingPlayer:
                    state2[i][e] = 1
                    res.append(copy.deepcopy(state2))
                else:
                    state2[i][e] = -1
                    res.append(copy.deepcopy(state2))
    
    return res


def render(state):
    for row in state:
        print(row)
    print(" ")


def miniMax(state, depth, maximizingPlayer):

    terminal, heuristicValue = isTerminal(state)
    bestChild = None  

    if depth == 0 or terminal:
        return heuristicValue, bestChild
    
    if maximizingPlayer:
        bestValue = float("-inf")
        for child in childrens(state, maximizingPlayer):
            v, _ = miniMax(child, depth-1, False)
            if v > bestValue:
                bestValue = v
                bestChild = child  
        return bestValue, bestChild
        
    else:
        bestValue = float("inf")
        for child in childrens(state, maximizingPlayer):
            v, _ = miniMax(child, depth -1, True)
            if v < bestValue:
                bestValue = v
                bestChild = child  
        return bestValue, bestChild
    
def parseInput():
    str = input("Introduzca las coordenadas dnd quiere poner su ficha: ")
    str2 = str.split(" ")
    return int(str2[0])-1, int(str2[1])-1


def comprobarTerminal(state):
    t, v = isTerminal(state)
    if t:
        if v == 0:
            print("###########################################################")
            print("##                  EMPATE                               ##")
            print("###########################################################")
            render(state)
        
        elif v == 1:
            print("################################################################")
            print("##                      HAS PERDIDO                           ##")
            print("################################################################")
            render(state)


        return t
    else:
        return t

def play():

    depth = 1000
    state = [[0,0,0],[0,0,0],[0,0,0]]
    render(state)
    c = 1

    while True:
        n,m = parseInput()
        state[n][m] = -1
        print(f"JUGADA {c} HUMANO ------------------------------------")
        c += 1
        if comprobarTerminal(state):
            break
        render(state)        

        v, state = miniMax(state,depth,True)
        print(f"JUGADA {c} MÁQUINA ------------------------------------")
        if comprobarTerminal(state):
            break
        c+=1
        render(state)


if __name__ == "__main__":
    play()