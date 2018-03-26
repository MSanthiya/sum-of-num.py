num= int(input("enter a number"))
sum=0
if(num<=0):
	print("enter a positive number")
for j in range(1,num+1):
	sum=sum+j
print(sum)
