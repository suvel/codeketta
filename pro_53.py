import string
 
def ispangram(s, a=string.ascii_lowercase):
    a= set(a)
    return a <= set(s.lower())
 
if  ispangram(input())== True:
	print("yes")
else:
	print("no")
