import math

def MadMax(N, Tele):
   
    exchange=0
    for j in range(N):
     for i in range(N-1):
        if (Tele[i]>Tele[i+1]):
            exchange=Tele[i+1]
            Tele[i+1]=Tele[i]
            Tele[i]=exchange
    exchange=0
    print(Tele)
      
    for i in range(math.ceil((N-1)/4)):
            exchange=Tele[i+int((N-1)/2)]
            Tele[i+int((N-1)/2)] = Tele[N-(i+1)]
            Tele[N-(i+1)] = exchange
            
   
    return Tele
