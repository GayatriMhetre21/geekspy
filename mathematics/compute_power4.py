def power(x,n):
    if(n==0):
        return 1
    if(x==0):
        return 0
    return x*power(x,n-1)

if __name__ == "__main__":
    x=2
    n=3
    print(power(x,n))