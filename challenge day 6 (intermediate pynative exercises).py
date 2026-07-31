# Practice Problem 1: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4
#characters, and converts the remaining strings to uppercase.

##words = ["apple", "bat", "cherry", "dog", "elderberry"]
##filterd_words = [ w.upper() for w in words if len(w) >= 4 ]
##
##print(f"Original: {words}")
##print(f"Result: {filterd_words}")

#Practice Problem 2: Write a function that merges two dictionaries. If a key exists in both
#dictionaries, sum their values. If a key exists in only one, include it as is.

##def merge_dicts (d1 , d2):
##    result = d1.copy()
##
##    for key, value in d2.items():
##        result [key] = result.get (key,0) + value
##    return result
##
##dict_a = {'a': 10, 'b': 20}
##dict_b = {'b': 5, 'c': 15}
##
##merged = merge_dicts(dict_a, dict_b)
##print(f"Merged Dictionary: {merged}")


# Practice Problem 3: Create a function that takes a string and returns
#a count of how many times each character appears. Ignore spaces
#and make it case-insensitive.

##from collections import Counter
##def get_frequency (input_string):
##    clean_text = input_string.lower().replace(" ", "")
##
##    return Counter(clean_text)
##
##text = "Python Programming"
##freq = get_frequency(text)
##
##print(f"Original: {text}")
##print(f"Character Frequency: {freq}")

#Practice Problem 4: Write a function that determines if two strings
#are anagrams (contain the exact same characters in a different order).

##def is_anagram (str_1,str_2):
##    s1 = sorted (str_1.lower().replace(" ", ""))
##    s2 = sorted (str_2.lower().replace(" ", ""))
##
##    return s1 == s2
##
##w1, w2 = "listen", "silent"
##result = is_anagram(w1, w2)
##
##print(f'Is "{w1}" an anagram of "{w2}"? {result}')

# Practice Problem 5: Write a recursive function that takes a list
#containing other lists (of any depth) and returns a single “flat”
#list of all elements.

##def flatten(lst):
##    flat_list = []
##
##    for item in lst:
##        if isinstance(item,list):
##            flat_list.extend(flatten(item))
##        else:
##            flat_list.append(item)
##    return flat_list
##
##nested_data = [1, [2, 3], [4, [5, 6]], 7]
##result = flatten(nested_data)
##
##print(f"Original:  {nested_data}")
##print(f"Flattened: {result}")


# Practice Problem 6: Given a sentence, reverse each individual word
#within the string while maintaining the original word order.

##def reverse_individual_words(sentence):
##    words = sentence.split()
##
##    reversed_words = [word[::-1] for word in words]
##
##    return " " .join(reversed_words)
##
### Usage
##text = "Python is awesome"
##result = reverse_individual_words(text)
##print(f"Original: {text}")
##print(f"Result:   {result}")
    

# Practice Problem 7: Write a function to check if a full sentence is a
#palindrome. You must ignore case, spaces, and all punctuation marks.

##def is_palindrome_sentence (sentence):
##   clean_chars = [char.lower() for char in sentence if char.isalnum()]
##
##    # Join into a string
##   clean_str = "".join(clean_chars)
##    
##    # Compare with its reverse
##   return clean_str == clean_str[::-1]
##
### Usage
##test_s = "A man, a plan, a canal: Panama"
##print(f"Is palindrome? {is_palindrome_sentence(test_s)}")

# Practice Problem 8: Given a list of strings, use a single list comprehension
#to extract strings that meet two criteria: they must be longer than 5
#characters AND they must start with a vowel (a, e, i, o, u).
    
##words = ["apple", "education", "ice", "ocean", "python", "umbrella"]
##
##vowel_long = [
##    s for s in words if len(s) > 5 and s[0].lower() in 'aeiou'
##    ]
##print(f"Original: {words}")
##print(f"Filtered: {vowel_long}")


# Practice Problem 9: Write a function that removes duplicate elements from
#a list. You cannot use set() because sets do not maintain the original
#order of elements.

##def remove_duplicates_ordered(items):
##    seen = set()
##    result = []
##    
##    for x in items:
##        if x not in seen:
##            result.append(x)
##            seen.add(x)
##            
##    return result
##
### Usage
##nums = [1, 2, 2, 3, 1, 4, 2]
##print(f"Cleaned List: {remove_duplicates_ordered(nums)}")


# Practice Problem 10: Create a function rotate_list(lst, n, direction) that shifts
#the elements of a list by N positions. The direction can be ‘left’ or ‘right’.

def rotate_list(lst, n, direction='right'):
    if not lst:
        return lst
        
    # Handle shifts larger than the list length
    n = n % len(lst)
    
    if direction == 'right':
        # Take the last n elements and put them at the front
        return lst[-n:] + lst[:-n]
    else:
        # Take the first n elements and put them at the back
        return lst[n:] + lst[:n]

# Usage
data = [1, 2, 3, 4, 5]
print(f"Right Shift 2: {rotate_list(data, 2, 'right')}")
print(f"Left Shift 1:  {rotate_list(data, 1, 'left')}")

