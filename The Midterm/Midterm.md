f# Programming in Science — Midterm Test A

**Time:** 75 minutes  
**Total:** 30 marks  
**Theory:** 15 marks  
**Programming:** 15 marks  
**VS Code:** Allowed  
**pytest:** Not used anywhere on this test.

## Instructions

- Answer all questions.
- Show your reasoning for theory questions.
- For programming questions, write ordinary Python functions.
- You may use VS Code to write, run, and debug your code.
- You are responsible for understanding your solution.
- Use only programming concepts covered by the syllabus.
- No pytest, unit-test framework, or test file is required.
 


---

# Part A — Theory (15 marks)

## Q1 — Input, Split, and Conversion (2 marks)

Consider:

```python
a, b, c = input("Values: ").split()
a = int(a)
b = float(b)
```

The user enters:

```text
12 4.5 hello
```

State the final **value and type** of `a`, `b`, and `c`.
ANSWER
a = 12, int -> we converted it to an integer using int()
b = 4.5, float  -> we converted it to a float using float()
c = "hello", str -> it remains a string because we did not convert it to any other type.
---

## Q2 — Arithmetic and Built-in Functions (2 marks)

Without running:

```python
x = -12.7
print(abs(x))
print(int(x))
print(round(x))
```


The three values printed are:
- 12.7 -> absolute value of x removes the negative sign
- -12 -> integer conversion removes the decimal part
- -13 -> rounding to the nearest integer
"""
---

## Q3 — Conditional Boundary (2 marks)

What is printed? A

```python
score = 70

if score > 70:
    print("A")
elif score == 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("D")
```

What would be printed if the first condition were changed to:


```python
if score >= 70:
```
what would be printed is "A"; before this change, the expected out output was "B" 
---
# initially, the program without the change would print "B" because the first condition `score > 70` is false,
# so it checks the next condition `score == 70`, which is true, and prints "B".
# what would be printed if the first condition was changed to `if score >= 70:` is "A"; 
# the first condition would be true and the program would print "A" and not check the other conditions.


## Q4 — Loop Trace (2 marks)

Determine the final value of `total`.

```python
total = 0

for n in range(2, 10, 2):
    if n == 6:
        continue

    total += n
```
ANSWER : 14
final value of total is 14; with this program, we incremented the total by 2, 4, and 8,skipping 6 due to the continue statement. Thus, the final value of total is 14.---

## Q5 — String Indexing and Slicing (2 marks)

Given:

```python
text = "PYTHON"
```

Determine:

```python
text[0]
text[-1]
text[1:5]
text[::2]
text[::-1]
```

text = "PYTHON"

# Determine:

ANSWER
text[0] = #P: index 0 gives us the first character of the string, which is P
text[-1] = #N index -1 gives us the last character of the string, which is N
text[1:5] = #YTHO [1:5] gives us the characters from index 1 to index 4 (5 is not included), which is YTHO

text[::2] = #PTO [::2] takes every second character from the string
text[::-1] = #NOHTYP [::-1] reverses the string


---

## Q6 — String Processing (2 marks)

Determine the values of `words` and `result`.

```python
text = "red,green,blue"

words = text.split(",")
result = "|".join(words)
```
# red|green|blue -> we split the string into a list of words using the comma
#  then joined the list back into a string using | character.---

## Q7 — List Mutation (3 marks)

Determine the final output:

```python
values = [3, 5, 7]

values.append(9)
values[1] = values[0] + values[2]

print(values)
```
answer = #final output is [3, 10, 7, 9]
Then answer:

> What is the difference between `values.append(9)` and `values[1] = ...`?
# values.append(9) adds the value 9 to the end of the list.
# values[1] = ... replaces the value at index 1 with a new value, keeping the list length the same.

---

# Part B — Programming Challenges (15 marks)

## Q8 — String Challenge (3.75 marks)

Write:

```python
def extract_digits(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    return result

print(extract_digits("Room 204B"))  # Output: "204"; only digits stay
print(extract_digits("A1-B2-C3"))  # Output: "123"
print(extract_digits("No numbers"))  # Output: ""; no digit so empty list

```

Return a new string containing only the digit characters from `text`.

Examples:

```python
extract_digits("Room 204B") → "204"
extract_digits("A1-B2-C3") → "123"
extract_digits("No numbers") → ""
```

Do not convert the entire string to an integer.

---

## Q9 — List Challenge (3.75 marks)

Write:

```python
def cap_values(numbers, maximum):
    new_list = []
    for num in numbers:
        if num > maximum:
            new_list.append(maximum)
        else:
            new_list.append(num)
    return new_list

print(cap_values([4, 12, 7, 20], 10))  # Output: [4, 10, 7, 10]
print(cap_values([55, 67, 80, 20], 10))  # Output: [10, 10, 10, 10]
```

Return a **new list**.

- If a value is greater than `maximum`, replace it with `maximum`.
- Otherwise leave it unchanged.

Example:

```python
cap_values([4, 12, 7, 20], 10)
→ [4, 10, 7, 10]
```

Do not modify the original list.

---

## Q10 — Loop + Condition Challenge (3.75 marks)

Write:

```python
def sum_multiples(limit):
    total = 0
    number = 1
    while number <= limit:
        if (number % 3 == 0 and number != 12):
            total += number
        number += 1
    return total

print(sum_multiples(10))  # Output: 18
print(sum_multiples(12))  # Output: 18
print(sum_multiples(15))  # output: 33
print(sum_multiples(-10)) # output: 0 because the limit is negative,
#so the loop will not execute and the total will remain 0.
```

Starting at 1 and going through `limit`, calculate the sum of numbers divisible by 3.

However, **do not add the number 12**, even though it is divisible by 3.

Example:

```python
sum_multiples(10)
→ 18
```

because:

```text
3 + 6 + 9 = 18
```

---

## Q11 — Mixed String/List Challenge (3.75 marks)

Write:

```python
#ANSWER
def count_words_starting_with(words, letter):
    count = 0
    for word in words:
        if word.lower()[0] == letter.lower():
            count += 1
    return count

words = ["Apple", "ant", "Banana", "apricot", "pear", "potato:", "brocoli", "Brodie"]
wordy = [] # empty list

print(count_words_starting_with(words, "a")) # expected output: 3 #actual output: 0
print(count_words_starting_with(words, "b")) # expected output: 3
print(count_words_starting_with(words, "p")) # expected output: 2
print(count_words_starting_with(wordy, "a")) # expected output: 0
```

Return how many words in the list start with `letter`, ignoring capitalization.

Example:

```python
words = ["Apple", "ant", "Banana", "apricot", "pear"]

count_words_starting_with(words, "a")
→ 3
```

Your function should work with an empty list.

