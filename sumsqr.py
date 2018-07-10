try:
    j=int(input())
    i=int(j)
    sum=0
    while(i>0):
		sum=sum+((i%10)**2)
		i=i/10

    print(sum)
except ValueError:
    print("This is not a whole number.")
