x=int(input("Enter x:"))
result=0
while x>0:
    x=x//10
    result=result+1
print("Count of digits :"+str(result))