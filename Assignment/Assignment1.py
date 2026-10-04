# Code by Rania Sid and Amr Mousattat
# task 1
def classifyNumber(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# def classifyNumberLength(num):
#     if (abs(num) < 40 and not (num == 0)):
#         return "small"
#     elif (num == 0):
#         return ""
#     return "large"
 

# length = classifyNumberLength(number)
# print(f"The number {number} is a {length} {result}.")

# task 2

def print_star_shape(rows):
    result = ""
    for i in range(rows):
        result += ("*" * (i+1) + "\n")
    return result

#for pytest: check the length of the last row for the pytest


# # Post submission
# def print_star_shape_Reverse(num):  
#     result = ""
#     for i in range(num, 0, -1):
#         result += ("*" * i + "\n")
#     return result

# number = int(input("Enter a number: "))
# print (print_star_shape_Reverse(number))

# Task 3 -- Multiple of 3
def describe_multiplie(limit):
    while limit > 0:
        if limit % 3 == 0:
            print("multiple of 3 ")
        limit -= 1


# Task 4 -- Sum of even numbers

def sum_even(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total



if __name__ == "__main__":

    number = float(input("Enter a number: "))
    result = classifyNumber(number)
    print(result)

    number = int(input("Enter a number: "))
    print (print_star_shape(number))

    limit = int(input("Enter a number: "))
    describe_multiplie(limit)


    # limit = int(input("Enter a number: "))
    # describe_multiplie(limit)

    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: ")) 
    print (sum_even(start, end))
# Put the thing in pytest
# print (sum_even(1,10))

# print (sum_even(4,8))
