import math


def  squirrel(N): 
    k=  len(str(math.factorial(N)))
    return math.factorial(N) // (10 ** (k-1))
    
