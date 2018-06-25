def sum(a,b):
	print("Sum of Numbers are ", a+b)
def diff(a,b):
	if (a>b):
		print("Difference of Numbers are ",a-b)
	else:
		print("Difference of Numbers are ",b-a)
def prod(a,b):
	print("Product of Numbers are ", a*b)
def div(a,b):
	if (b!=0):
		print("Division of Numbers are ", a/b)

print("Enter your Choice:")
print("Sum:1")
print("Difference:2")
print("Product:3")
print("Division:4")
choice= int(input())

print("Enter First No.: ")
c=int(input())
print("Enter Second No.: ")
d=int(input())

if (choice==1):
	sum(c,d)
else:
	if (choice==2):
		diff(c,d)
	else:
		if (choice==3):
			prod(c,d)
		else:
			div(c,d)