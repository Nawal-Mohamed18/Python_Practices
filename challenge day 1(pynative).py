#Practice Problem 1: Write a Python function that accepts two integer numbers.
#If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

##number1 = int(input("Enter first number: "))
##number2 = int(input("Enter second number: "))
##
###function
##def product_sum (num1, num2):
##    product = num1 * num2
##
##    if product <= 1000:
##        return product
##    else:
##        return num1 + num2
##
###calling the function
##result = product_sum(number1 , number2)
##
###print the result
##print(result)


#Practice Problem 2: Iterate through the first 10 numbers (0–9).
#In each iteration, print the current number, the previous number, and their sum

##previous_num = 0
##
##for i in range(10):
##    current_num = i
##    sum_result = previous_num + current_num
##    
##    print(f"Current number: {current_num} previous number: {previous_num} Sum: {sum_result}")
##
##    previous_num = i 


#Practice Problem 3: Display only those characters which are present at
#an even index number in given string.

##string = input("Enter text (only string): ")
##
##for char in string[::2]:
##    print(char)
##    


#Practice Problem 4: Write a function to remove characters from a string starting
#from index 0 up to n and return a new string

##print("---Remove characters from a string---")
##
##word = str(input("Enter a word: "))
##num = int(input("Enter how many characters you want to remove: "))
##
##def remove_char (word, num):
##    word = word[num:]
##    
##    return word
##
### calling the function   
##function = remove_char (word,num)
##print(function)
    

# Practice Problem 5: Write a program to swap the values of two variables, a and b,
#without using a third temporary variable

##a = "nawal"
##b = 19
##
##print(f"Before swap: a = {a}, b = {b}")
##
##a,b = b,a
##
##print(f"After swap: a = {a}, b = {b}")


#Practice Problem 6:
#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

##number = int(input("Enter a number to calculate its factorial: "))
##factorial = 1
##for i in range(1,number + 1):
##    factorial = factorial * i
##    
##print(f"The factorial of {number} is {factorial}")

##num = int(input("Enter a number to calculate its factorial: "))
##factorial = 1
##
### Loop from 1 to num (inclusive)
##for i in range(1, num + 1):
##    factorial = factorial * i
##
##print(f"The factorial of {num} is {factorial}")    
##
    
#Practice Problem7: Create a list of 5 fruits. Add a new fruit to the end of the list,
#then remove the second fruit (at index 1).

##fruits = ["apple", "banana", "cherry", "date", "elderberry"]
##fruits.append("fig")
##fruits.pop(1)
##
##print(fruits)


# Practice Problem8: Write a program that
#takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

##string = str(input("Enter string text: "))
##print(f"Original text: {string}")
##print(f"Reversed text: {string [::-1]})

#Practice Problem9: Write a program to count the total
#number of vowels (a, e, i, o, u) present in a given sentence.

sentence = str(input("Enter a sentence to know the total vowels in it: "))

vowels ="aeiou"
count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1
        
print(f"Number of vowels: {count}")        
