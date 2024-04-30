# 1
# 2 2
# 3 3 3
# Algorithm
# 1. start with varibale rows which will represnt in how many rows, we need to print the pattern
# 2. iterate i from 1 to rows
# 3. Inside the loop we need print  i times the value of i

def print_pattern(rows):
    for i in range(1, rows+1):
        print((str(i) + " ") * i)

print_pattern(5)
print("Hi " * 5 )