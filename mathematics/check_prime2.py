def isprime(n):
    if(n<=1):
        return False
    if(n<=3):
        return False
    if(n%2==0 or n%3==0):
        return False
    
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):
            return False
        i=i+6
    return True
if (isprime(11)):
    print("true")

else:
    print("false")
if (isprime(15)):
    print("true")

else:
    print("false")