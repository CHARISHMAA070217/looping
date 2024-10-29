'''
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
n=int(input())
if(n>=100 and n<=999):
    a=n//10
    b=a%10
    if(b%3==0):
        print("Trendy Number")
    else:
        print("Not a Trendy number")
else:
    print("Not a Trendy Number")



'''
