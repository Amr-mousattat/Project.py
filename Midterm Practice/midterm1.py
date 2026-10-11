# Q1- types and conversion 
# x, y, z = input("Values: ").split()
# x = int(x)
# y = float(y)
# if users enters 5 2.5 hello
# then x is integer, y is float and z is string 

# a = 7.8, b = -7, c = -8

# Q3 - what is printed
temperature = 0

if temperature > 0:
    print("above")
elif temperature == 0:
    print("exactly")
else:
    print("below")

#"exactly" is going to be printed

# Q4 - Loop Trace
total = 0

for n in range(1, 7):
    if n % 2 == 0:
        total += n

#what will n be equal to? the sum of even numbers: so 2,4 and 6
#total sum is 12

#Q5 — String Indexing and Slicing (2 marks)
word = "COMPUTER"
word[1] # o
word[-2] # E
word[1:6:2] # OPT
word[::-1] # Retupcom
print(word[::-1])

#Q6 — String Methods and Splitting (2 marks)
text = "  Red,Green,Blue  "

a = text.strip() # removes all the spacings -> so "Red,Green,Blue"
b = a.split(",") # "red" , "green", "Blue"
c = "-".join(b) # c = "Red-Green-Blue"
# What are the values of a, b, and c?

#Q7 — List Mutation and Aliasing (3 marks)
numbers = [2, 4, 6]
other = numbers

other.append(8)
numbers[0] = 10

print(numbers)
print(other)
#What numbers will be printed? 
#numbers: [10, 4 ,6]
#other: [10,4,6,8]

#Part B — Programming (15 marks)


def clean_code(text):
    result = ""
    for char in text:
        if char.isalnum():
            result += char.upper()
    print(result)
        

"""
clean_code("Lab-5: Python!") → "LAB5PYTHON"
clean_code("A 1-b") → "A1B"
"""
clean_code("Lab-5: Python!")


"""
Return a new list:

values below 10 become 10;
values from 10 through 20 stay unchanged;
values above 20 become 20.

adjust_measurements([7, 10, 15, 23])
→ [10, 10, 15, 20]
"""
def adjust_measurements(values):
    result = []
    for i in values:
        if(i <= 10):
            result.append(10)
        elif(i <= 20):
            result.append(i)
        else:
            result.append(20)
    return result

print(adjust_measurements([7, 10, 15, 23]))

"""
Starting at 1:

add odd numbers;
subtract even numbers;
stop immediately when the running total becomes greater than 10 or less than -10;
return the total.
"""
def alternating_total(limit):
    total = 0
    number = 1

    while number <= limit:
        if(number % 2 == 1):
            total += number
        if(number % 2):
            total -= number
        if(abs(number) >= 10):
            break
        number += 1
    return total

"""
Q11 — Mixed String + List Challenge (3.75 marks)
Split the sentence into words and return the number of words whose length is strictly greater than limit.
count_long_words("Python makes programming interesting", 6) → 2
"""
def count_long_words(sentence, limit):
    words = sentence.split()
    count = 0 

    for word in words:
        if(len(word) > limit):
            count += 1
    
    return count

def count_long_wordsB(sentence, limit):
    return sum(1 for word in sentence.split() if len(word) > limit)

print(count_long_wordsB("Python makes programming interesting", 6))


