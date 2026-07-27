##Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration,
##print the current number, the previous number, and their sum

#method 1
##for i in range(0,10):
##    curr_num = i
##    prev_num = i-1
##    
##    if prev_num<0:
##        prev_num=0
##    add = curr_num+prev_num    
##    print(f"Current number {curr_num} Previous Number {prev_num} Sum: {add} ")

#method 2

print("Printing current and previous number sum in a range(10)")
previous_num = 0

# Loop from 0 to 9
for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}")
    
    # Update previous_num for the next iteration
    previous_num = i
