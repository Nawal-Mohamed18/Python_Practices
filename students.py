# students = {
#     "Name": "Nawal",
#     "Major": "Computer Science",
#     "University": "Hormuud University"
# }
# print(f"Your name is: {students['Name']}\nYour major is: {students['Major']}\nYour University is: {students['University']}")

# number = int(input("Enter a number: "))

# numbers = [1,2,3,4,5]

# def print_number_x_by_2(n):
#     result = n * 2
#     print(f"the number multiplied by 2 is: {result}")

# for n in numbers:
#    print_number_x_by_2(n)    

number_list = [1,2,3,4,5,6,7,8,9,10]

# def filter_evens(list_name):
#     even_numbers = []
#     for number in list_name:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers

# result = filter_evens(number_list)   
# print(result)

def filter_evens(list_name):
    return [number for number in list_name if number % 2 == 0]

result = filter_evens(number_list)   
print(result)

