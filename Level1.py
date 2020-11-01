import math


def PatternUnlock(N,hits):
   
    arr_index=[]
    arr_search = [[6,1,9],[5,2,8],[4,3,7]]
    length =  float(0)
    
    for i in range(N):
        current_number = hits[i]
        for k in range(3):
            for j in range(3):
                if (arr_search[k][j] == current_number):
                  arr_index.append(k)
                  arr_index.append(j)
    
    i=0
    while (i < len(arr_index) -3):
        if (abs(arr_index[i+2] - arr_index[i]) ==abs(arr_index[i+3] - arr_index[i+1]) ):
            length =length+math.sqrt(2)

        else:
            length=length+float(1)
        i+=2
    length= round(length,5)    
    
    str_numb=str(length)
    bad_chars =['.', '0']
    for i in bad_chars : 
        str_numb = str_numb.replace(i, '') 
    
    
    return str_numb


