A = [5, 2, 4, 6, 1 ,3]

def InsertionSort(n):
   j=1
   for j in range(len(n))  :
      key = n[j] 
      n[j]=n[j-1]
      i=j-1
      while i>=0 and n[i]>key :
         n[i+1]=n[i]
         i=i-1
      n[i+1]=key
   return n

print(InsertionSort(A))
  
    
 