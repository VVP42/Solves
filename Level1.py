

def SynchronizingTables(N, ids,salary):
   
    exchange=0
    i=0
    j=0
    
    
    for j in range(N):
             
        for i in range(N):
            if ( (ids[j] > ids[i] and salary[j] < salary[i]) or (ids[j] < ids[i] and salary[j] > salary[i]) ):
                exchange = salary[i]
                salary[i] = salary[j]
                salary[j] = exchange
           
            
    
      
   
    return salary

