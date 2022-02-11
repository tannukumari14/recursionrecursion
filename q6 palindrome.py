# def Palindrome():
#     i=int(input("enter the number"))
#     a=0
#     b=i
#     while i>0:
#         a=(a*10)+i%10
#         i=i//10
#     if b==a:
#         return "palindrome number"
#     else:
#         return "not palindrome"
# print(Palindrome()

def reverse(str1):
    if len(str1)==1:
        return str1
    else:
        return reverse(str1[1:])+str1[0]
str1=input("enter the string")
str2=reverse(str1)
print(str2)
if str1==str2:
    print(str1,"it is palindrome no")
else:
    print(str1,"not a palindrome no")
    