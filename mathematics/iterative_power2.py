def power(x,y):
    res=1
    while(y>0):
        if((y&1)==1):
            res=res*x
        y=y>>1
        x=x*x

    return res
x=3
y=5
print("power is ",power(x,y))