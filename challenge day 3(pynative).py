# Practice Problem 18: Write a program to extract each digit from an integer in the reverse order.
  # 1. By converting into string
##int_num = int(input("Enter an integer value: "))
##
##str_num =  str(int_num)
##reversed_str = str_num[::-1]
##for digit in reversed_str:
##        print(digit)

   # 2. By using modulo % and floor division //

##num = int(input("Enter an integer value: "))
##print(f"Given number: {num}")
##while num > 0:
##    
##    last_digit = num % 10
##
##    num = num // 10 # chop off the last digit
##
##    print(last_digit, end = "  ")


# Practice Problem 19: Calculate income tax for a given income based
#on these rules:
##First $10,000: 0% tax
##Next $10,000: 10% tax
##Remaining income: 20% tax

##while True:
##    income = float(input("Enter an income to calculate income tax: "))
##
##    tax_payable = 0
##
##    if income <= 10000:
##        tax_payable = 0
##    elif income <= 20000:
##        tax_payable = (income - 10000) * 10 / 100
##
##    else:
##        tax_payable = 0 + (10000 * 10/100)
##        tax_payable += (income - 20000) * 20 / 100
##        
##    print(f"Total income to pay is: {tax_payable}")


# Practice Problem 20: Print a multiplication table from 1 to 10
#in a formatted grid.

##print(f"===Multiplication Table===")
##for columns in range(1,11):
##    for rows in range(1, 11):
##        print(columns * rows, end = "\t")
##    print("\n")    
    
        
# Practice Problem 21: Print a downward half-pyramid pattern using stars (*).

for i in range(5,0,-1):
    for j in range(0,i):
        print("*", end = " ")
    print("\n")    
        
        

        
    






    
