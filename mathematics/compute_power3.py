def power(x,n):
    for i in range(n):
        power=power * x
    return power

if __name__ == "__main__":
    x=2
    n=3
    print(power(x,n))