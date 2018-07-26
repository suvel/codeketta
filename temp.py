def f(m,n,o):
	for i in range(m,n,o):
		t_b=t_b-1
		if(f==i):
			if(t_b>(i+(i-f))):
					pass
			else:
				t_b=b
				count=count+1
	return 0


a,b,f,k=input().split()
a,b,f,k=int(a),int(b),int(f),int(k)
t_b=b
count=0
while(k>0):
	f(0,a,1)
	k=k-1
print(count)
