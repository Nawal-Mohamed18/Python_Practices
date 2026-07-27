 #String Indexing and Even Slicing
#Display only those characters which are present at an even index number in given string

##string=(input("Enter string only: "))
##
##start = 0
##stop = len(string) - 1
##step = 2
##
##
##
##for s in str(string):
##    
##    print(string[start])
##    
##    for n in range(start,step,stop):
##        print(string)

word = str(input("Enter string only: "))
print("Original String is ", word)

# Method: Using list slicing
# format: [start:stop:step]
even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)
