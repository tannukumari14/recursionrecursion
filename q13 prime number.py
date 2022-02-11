def prime(num,i):
    if i==1:
        return 1
    elif num%i==0:
        return 0
    return prime(num,i-1)
num=int(input("enter the number"))
n=prime(num,int(num/2))
if n==1:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    