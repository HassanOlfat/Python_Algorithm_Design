A = [5, 2, 4, 6, 1 ,3]
j=1
for j in range(len(A))  :
     key = A[j] 
     A[j]=A[j-1]
     i=j-1
     while i>=0 and A[i]>key :
        A[i+1]=A[i]
        i=i-1
     A[i+1]=key

print(A)
  
    
 