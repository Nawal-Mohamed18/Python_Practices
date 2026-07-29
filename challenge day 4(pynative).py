# Practice Problem 22: Write a function called exponent(base, exp) that returns an integer value of the
#base raised to the power of the exponent.

##def exponent(base, exp):
##    num = exp
##    result = 1
##    while num > 0:
##        
##        result = result * base
##        num = num -1
##        
##
##    print(f"{base} raises to the power of {exp}: {result}")
##    
##exponent (2,5)
##exponent (5,4)  

# Practice Problem 23: Write a program to check if a given number is a palindrome.
#A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

# using modulo and division floor

##number = int(input("Enter an integer number: "))
##original_number = number
##reversed_number = 0
##
##while number > 0:
##    last_digit = number % 10
##
##    reversed_number = (reversed_number * 10) + last_digit
##
##    number = number // 10
##
##if original_number == reversed_number:
##    print(f"{original_number} is a palindrome.")
##else:
##    print(f"{original_number} is not a palindrome.")

    
# Practice Problem 24: Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1,
#and each subsequent number is the sum of the two preceding ones.

##terms = int(input("Enter terms: "))
##
##num1, num2 = 0,1
##
##
##for i in range(terms):
##    print(num1, end = " ")
##    res = num1 + num2
##    num1 = num2
##    num2 = res

# Practice Problem 25: Write a program that takes a year as input and determines
#if it is a leap year.


##year = int(input("Enter a year: "))
##
##if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
##        print(f"{year} is a leap year.")
##else:
##    print(f"{year} is not a leap year.")

# Practice Problem 26: Write a program that takes
#two separate dictionaries and merges them into one single dictionary.

##dict1 = {"name": "Alice", "age": 25}
##dict2 = {"city": "New York", "job": "Engineer"}
##
##new_dict = dict1 | dict2 #simple combining by | symbol
##print(new_dict)
##
##new_dict.clear() # just to clear the new_dict
##
##new_dict.update(dict1) # older method .update()
##new_dict.update(dict2)
##print(new_dict)

# Practice Problem 27: Take two lists and find the elements that appear in both.
#Use Sets to perform the operation

##list_a = [1, 2, 3, 4, 5]
##list_b = [4, 5, 6, 7, 8]
##
##set_a = set(list_a)
##set_b = set(list_b)
##
##common_elements = set_a & set_b
##
##print(common_elements)

#Practice Problem 28: Start with a list of 10 numbers. Iterate through them and sort
#them into two separate lists: one for even numbers and one for odd numbers.

##numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
##even_numbers = []
##odd_numbers = []
##
##for i in numbers:
##    if i % 2 == 0:
##        even_numbers.append(i)
##    else:
##        odd_numbers.append(i)
##
##print(f"Even numbers: {even_numbers}\nOdd_numbers: {odd_numbers}")


# Practice Problem 29: Create a list of 5 words. Write a loop that iterates through the
#list and prints each word alongside its character count.

##words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
##
##length = 0
##for word in words:
##    length = len(word)
##   
##    print(word,length)


# Practice Problem 30: Write a program that counts how many times each word appears
#in a given paragraph and stores these counts in a dictionary.

text = "apple banana apple cherry banana apple"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)
    
