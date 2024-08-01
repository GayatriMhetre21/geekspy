def palindrome(n):
    reverse=0
    temp=n
    while (temp!=0):
        reverse=(reverse*10)+(temp%10)
        temp=temp//10
    return(reverse==n)

n=7007
if(palindrome(n)==1):
    print("yes")
else:
    print("No")