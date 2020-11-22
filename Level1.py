
import textwrap as tw
import re
 

def WordSearch(leng, s, subs): 
   
   words = s.split()
   
   
   new_string =''
   now_str =''
   for i in range(len(words)):
       if len(words[i]) < leng and len(now_str) + len(words[i]) < leng:
           new_string+=' '
           now_str+=' '
           new_string += words[i]
           now_str+=words[i]
           
           continue
       if len(words[i]) < leng and len(now_str) + len(words[i]) > leng:
           now_str=''
           new_string+='\n '
           new_string += words[i]
           now_str+= words[i]
           continue
       
       if len(words[i]) >= leng:
           j =0
           k=0
           while j< len(words[i]):
            now_str=''
            new_string +='\n'
            new_string +=words[i][j:leng+k]
            
            j+=leng
            k+=leng
            #new_string+= words[i][leng+1:len(words[i])]
            #now_str+= words[i][leng:len(words[i])]
            #continue
           new_string +='\n'
       
       if len(now_str) >= leng:
           now_str=''
           new_string +='\n'
           new_string+=words[i]
           now_str+=words[i]
           continue
       
       

       word_sostavn=''
   str_search = new_string.split('\n')
   
   
   mass =list()
   current_number=0
   for i in range(len(str_search)):
       for j in range(len(str_search[i].split())):
         
         if  subs ==  str_search[i].split()[j]:
            current_number=1
            break
         else:
            current_number=0
       mass.append(current_number)

   
   return mass
   

   



