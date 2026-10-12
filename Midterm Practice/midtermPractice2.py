
#Q1
x = 15
y = 4

a = x / y
b = x // y
c = str(x) + str(y)
d = float(x % y)
print(a)
print(b)
print(c)
print(d)
#Q2
numbers = [-4, 7, -9, 2]

a = abs(min(numbers))
b = max(numbers) - min(numbers)
c = round(7.856, 1)
d = len(str(a * 10)) #90 so length of it is 

print(a, b, c, d)
#Q3
temperature = 25
humidity = 70

if temperature >= 20 or humidity < 60:
    print("A")
elif temperature > 30:
    print("B")
else:
    print("C")

if temperature < 30 and humidity >= 70:
    print("D")
#prediction:
# C
# D
#Q4
total = 0

for n in range(2, 12, 2): #2,4,6,8,10
    if n == 6:
        continue # the n got skipped over
    if n > 8:
        break
    total += n

print(total) # total = 12

#Q5
word = "PROGRAMMING"
#say the indext for each and what it will print
"""
a = word[2] -> "O"
b = word[-3] -> "I"
c = word[1:9:2] -> "RGAM"
d = word[::-2] -> "GIMROP"
"""

#Q6
#Determine the result of each expression:
text = "  Python,Java,C++  "

a = text.strip()
b = a.split(",")
c = b[0].lower()
d = "|".join(b)
"""
a = "Python,Java,C++" -> remove all the spacings
b = "Python", "Java", "C++" -> spliting the string into whatever number whenever a "," is encountered
c = "python", "Java", "C++" -> the string at index 0 is now lower cased
d = "python|Java|C++" -> joined up by "|"
"""

#Q7 - List Aliasing and Mutation (3 marks)
# What is printed by each print() statement?
numbers = [3, 6, 9]
other = numbers #same list 
copy = numbers[:] # A copy is lowkirkuenily created here 

other[1] = 12 #other and numbers are changed now
copy.append(15)
numbers.append(18) # 18 added to both numbers and other

print(numbers) # [3, 12, 9, 18]
print(other) # [3, 12, 9, 18]
print(copy) # [3, 6, 9, 15]
# since we did not actually make a copy, all three will be the same same 
# and will print out: 

# Part B - Programming

# Q8 — String Processing (3.75 marks)
"""
Your function must return a new string that follows these rules:
- Remove all spaces from the text.
- Convert all letters to uppercase.
- Replace every digit with #.
- Keep other characters unchanged.
"""
def format_identifier(text: str):
    result = ""
    a = "".join(text.split()).upper()
    for x in a:
        if x.isnumeric():
            result += "#"
        else: result += x

        
    return result

print(format_identifier("hello 56-python"))
print(format_identifier("Room 5-b"))
print(format_identifier("py charm 4%^"))

# Q9 — List Processing (3.75 marks)
"""
Your function receives a list of numbers and must:
- Ignore all negative numbers.
- Ignore zero.
- Multiply each remaining positive number by 2.
- Return a new list containing the results in their original order.
- Do not modify the original list.

filter_and_double([3, -2, 0, 7, -5, 4])
# [6, 14, 8]

filter_and_double([-1, -4, 0])
# []

filter_and_double([2, 5, 10])
# [4, 10, 20]
"""
def filter_and_double(values: list):
    result = []
    for x in values:
        if(x>0):
            result.append(x*2)
    return result

print(filter_and_double([3, -2, 0, 7, -5, 4]))
print(filter_and_double([-1, -4, 0]))
print(filter_and_double([2, 5, 10]))

#Q10
"""
Your function must:
- Start with number = 1 and total = 0.
- Add consecutive integers to total (1, 2, 3, 4, ...).
- Stop immediately when the total becomes greater than or equal to limit.
- Return the final total.
You must use a while loop.

sum_until_limit(10)
# 10   (1 + 2 + 3 + 4)

sum_until_limit(12)
# 15   (1 + 2 + 3 + 4 + 5)

sum_until_limit(1)
# 1
"""
def sum_until_limit(limit: int):
    number = 1
    total = 0
    while number <= limit:
        total += number
        number += 1

        if(total >= limit): break
    return total

"""
or 
def sum_until_limit(limit: int):
    number = 1
    total = 0

    while total < limit:
        total += number
        number += 1

    return total
    """
print(sum_until_limit(10))
print(sum_until_limit(12))
print(sum_until_limit(1))

# Q11 — Mixed Strings, Lists, and Conditions (3.75 marks)
"""
It must:
- Split the sentence into individual words.
- Select only words whose length is greater than or equal to minimum.
- Convert the selected words to uppercase.
- Return a new list containing those words in their original order.

analyze_words("Python is very useful", 4)
# ["PYTHON", "VERY", "USEFUL"]

analyze_words("I love programming in Python", 6)
# ["PROGRAMMING", "PYTHON"]

analyze_words("cat dog bird", 5)
# []
"""
def analyze_words(sentence: str, minimum: int):
    words = sentence.upper().split()
    result = []
    for word in words:
        if(len(word) >= minimum):
            result.append(word)
    return result

print(analyze_words("Python is very useful", 4))
print(analyze_words("I love programming in Python", 6))
print(analyze_words("cat dog bird", 5))
