#Practice Problem 10: Given a list of integers, find and print both the largest and the smallest numbers.

##nums = [45, 2, 89, 12, 7]
##
##print(f"Largest: {max(nums)} Smallest: {min(nums)}")

#Practice Problem 11: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

##data = [1, 2, 2, 3, 4, 4, 4, 5]
##
##print(f"Data: {data}")
##
##data_set = set(data)
##
##new_data = list(data_set)
##
##print(f"Unique data: {new_data}")

### precise way
##data = [1, 2, 2, 3, 4, 4, 4, 5]
##
### Set conversion removes duplicates automatically
##unique_data = list(set(data))
##
##print(f"Unique List: {unique_data}")

# Practice Problem 12: Write a function to return True if the first and last number
#of a given list is the same.If the numbers are different, return False.

##numbers_x = [10, 20, 30, 40, 10]
##numbers_y = [75, 65, 35, 75, 30]
##
##def classi_func(list_name):
##    first_num = list_name[0]
##    last_num = list_name[len(list_name)-1]
##
##    if first_num == last_num:
##        decision = True
##    else:
##        decision = False
##
##    print(f"Given list:{list_name} Result: {decision}")
##
###call the function 
##classi_func(numbers_x)
##classi_func(numbers_y)


#Practice Problem 13: Iterate through a given list of numbers and
#print only those numbers which are divisible by 5.

##num_list = [10, 20, 33, 46, 55]
##for number in num_list:
##    if number % 5  == 0:
##        print(number)
##    else:
##        continue
    

#Practice Problem 14: Write a program to find how many times
#the substring “Emma” appears in a given string.

##str_x = "Emma is good developer. Emma is a writer"
##
##count = str_x.lower().count("emma")
##print(f"Emma appeared {count} times.")

    
#Practice Problem 15: Print the following pattern where each row
#contains a number repeated a specific number of times based on its value.

##for num in range(1,6):
##    for i in range(num):
##        print(num, end=" ")
##    print("\n")


#Practice Problem 16: Write a program to check if a given number
#is a palindrome (reads the same forwards and backwards).

##num = int(input("Enter number: "))
##
##str_num = str(num)
##
##if str_num == str_num[::-1]:
##    print(f"Number {num} is a palindrome number.")
##else:
##    print(f"Number {num} is not a palindrome number.")

# Practice Problem 17: Create a new list from two given lists such that the new list
#contains odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []

for num in list1:
    if num % 2 == 0:
        continue
    else:
        result_list.append(num)

for i in list2:
    if i % 2 == 0:
         result_list.append(i)
    else:
        continue
print(f"Original lists: {list1}, {list2}")
print(f"Combined list: {result_list}")




