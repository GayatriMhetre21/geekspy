def isprime(n):
    if n==1:
        return False
    
    if n==2 or n==3:
        return False
    
    if n%2==0 or n%3==0:
        return False
    
    i=5
    while(i*i<=n):
        if n%1==0 or n%(i+2)==0:
            return False
        
        i+=6
    return True

def printprimes(n):
    for i in range(2,n+1):
        if isprime(i): 
            print(i,end=" ")
if __name__ == "__main__" :
    n=18
printprimes(n)