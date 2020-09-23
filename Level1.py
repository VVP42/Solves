



def ConquestCampaign(N,M,L, battalion):          
 
    matrix = [[0] * M for i in range(N)]
    ind=0
    k=0
    f=0
    while (ind<2*(L)):
        k=battalion[ind]
        f = battalion[ind+1]
        matrix[k-1][f-1]=1
        ind+=2
    print(matrix)
        
    
    
    count =1
       
    def is_zero(matrix,N,M):
        for i in range(N): 
          for j in range(M): 
             if (matrix[i][j]==0):
                 return 0

    while (is_zero(matrix,N,M)==0):
        
        for i in range(N): 
          for j in range(M): 
            if (matrix[i][j]>0):
                matrix[i][j]+=1

        for i in range(N): 
          for j in range(M): 
            if  (matrix[i][j]>=2):
                if (i>0 and matrix[i-1][j]==0):
                    matrix[i-1][j]+=1
                if (i<N-1 and matrix[i+1][j]==0):
                    matrix[i+1][j]+=1
                if (j>0 and matrix[i][j-1]==0):
                    matrix[i][j-1]+=1
                if (j<M-1 and matrix[i][j+1]==0):
                    matrix[i][j+1]+=1
        count+=1
    
             
    
    return count




