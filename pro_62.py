def chek(s):
    if(s==s[::-1]):
        return 1
    else:
        return 0
   
A=str(input())
s=list()
for i in range (len(A)):
    s.append(A[i])
for i in range (len(A)):   
    sr= ''.join(s)
    if(chek(sr)==1):
        pass
    else:   
        s.pop()

print(len(A)-len(s))    
