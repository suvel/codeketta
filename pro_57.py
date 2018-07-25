A,B=input().split()
A=str(A)
al=len(A)
B=str(B)
S=""

for i in range(al):
    S=S+A[i]
    if(S in B and len(S)>=2):
        print("yes")
        exit()
    elif(len(S)>=2):
        S=""
    else:
        pass

print("no")
