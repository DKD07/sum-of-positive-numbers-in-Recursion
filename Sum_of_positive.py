def Sum_of_positive(n):
    if n<=0:
        return 0
    else:
        return n+Sum_of_positive(n-2)
x=int(input("Enter the value of x: "))
output= Sum_of_positive(x)
print("the output is : ",output)