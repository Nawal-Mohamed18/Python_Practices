# Practice Problem 31: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found

###my way
##prime_list = [2,3,5,7,11,13,17,19]
##sliced_list = prime_list[::2]
##print(sliced_list)
##
###Another way
##primes = []
##
##for num in range(2, 21):
##    # Check if number is prime
##    for i in range(2, int(num**0.5) + 1):
##        if num % i == 0:
##            break
##    else:
##        primes.append(num)
##
### Print alternate primes
##alternate_primes = primes[::2]
##print(alternate_primes)

            
#Practice Problem 32: Create a dictionary where the keys are numbers
#from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).
##numbers = range(1,11)
##sq_dict = {}
##for i in numbers:
##    value = pow(i,2)
##    sq_dict[i] = value
##print(sq_dict)


# Practice Problem 33: Ask the user for a sentence. Replace every empty space in
#that sentence with an underscore (_) and print the final result.
##
##sentence = input("Enter a sentence: ")
##old = " "
##new = "_"
##
##print(sentence.replace(old,new))
##
### this way is also good
##user_sentence = input("Enter a sentence: ")
##
### Replace space with underscore
##sanitized_sentence = user_sentence.replace(" ", "_")
##
##print(sanitized_sentence)


# Practice Problem 34: Print a downward number pattern
#where each row starts with a decreasing value.

##rows = 5
### Outer loop for number of rows
##for i in range(rows, 0, -1):
##    # Inner loop for printing numbers in each row
##    for j in range(i, 0, -1):
##        print(j, end=' ')
##    print("") # New line

#Practice Problem 35: Write a program to check if a user-entered string
#contains any numeric digits. Use a for loop to examine each character
##flag = False
##input_string = str(input("Enter text: "))
##for char in input_string:
##   if char.isdigit():
##       flag = True
##       break
##print(f"The string '{input_string}' contains digits: {flag}")

# Practice Problem 36: Write a program to capitalize the first letter of each word
#in a given string without using the built-in .title() method.

##text = "hello world from python"
##
### Split the string into a list of words
##words = text.split()
##capitalized_words = []
##
##for word in words:
##    # Capitalize each word and add to the new list
##    capitalized_words.append(word.capitalize())
##
### Join the list back into a single string
##result = " ".join(capitalized_words)
##print(result)


# Practice Problem 37: Create a countdown timer that starts from a given number
#and counts down to zero using a while loop.

##import time
##
##count = 5
##
##while count > 0:
##    print(count)
##    # Pause the program for 1 second
##    time.sleep(1)
##    # Decrement the counter
##    count -= 1
##
##print("Blast off!")


# Practice Problem 38: Write a program that creates a new text file named notes.
#txt, writes three separate lines of text to it, and then reads that file back
#to display the contents in the console.    

##with open ("notes.txt", "w") as file:
##    file.write("Hello, this is my first note.\n")
##    file.write("Python file handling is simple.\n")
##    file.write("End of file.\n")
##
##print("Reading file contents: ")
##with open ("notes.txt", "r") as file:
##    content = file.read()
##    print(content)


#Practice Problem 39: Write a script that opens an existing .txt file and counts the
#total number of words it contains.

##try:
##    with open ("sample.txt", "r") as file:
##        data = file.read()
##        data_split = data.split()
##        length = len(data_split)
##        print(f"The file contains {length} words.")
##    
##except FileNotFoundError:
##    print("Error: The file 'sample.txt' was not found.")

    
# Practice Problem 40: Create a Car class with attributes for make, model, and
#year. Include a method called start_engine() that prints a formatted string
#describing the car starting up

class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine is now running!")


my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()
