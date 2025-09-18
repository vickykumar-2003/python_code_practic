# num = int(input("Enter a number:"))
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i
# print("Factorial of",num,"is:",fact)

# Using funtion Print Factorial number.....
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
num = int(input("Enter a number:"))
print("Factorial of",num,"is:",factorial(num))