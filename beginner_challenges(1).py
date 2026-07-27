##Write a Python function that accepts two integer numbers.
##If the product of the two numbers is less than or equal to 1000,
##return their product; otherwise, return their sum.

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

def my_func (num1,num2):
    if (num1*num2) <= 1000:
        return num1*num2
    else:
        return num1+num2

print(my_func(n1,n2))    
    
