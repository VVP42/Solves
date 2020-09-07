



def odometer(arr):
    
     length =0
    
     
     Diff_Hr = 0
     i=0
     while i< len(arr):
       if (i % 2 ==0):
           Current_Km = arr[i]
       else:
           Current_Hr = arr[i]-Diff_Hr
           length+= Current_Hr*Current_Km
           Diff_Hr = arr[i]
       i+=1
     return length

