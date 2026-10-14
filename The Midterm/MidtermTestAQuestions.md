# Programming in Science — Midterm Test A

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

---

## Q2 — Arithmetic and Built-in Functions (2 marks)

Without running:

```python
x = -12.7
print(abs(x))
print(int(x))
print(round(x))
```

What three values are printed?

---

## Q3 — Conditional Boundary (2 marks)

What is printed?

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

---

## Q4 — Loop Trace (2 marks)

Determine the final value of `total`.

```python
total = 0

for n in range(2, 10, 2):
    if n == 6:
        continue

    total += n
```

---

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

---

## Q6 — String Processing (2 marks)

Determine the values of `words` and `result`.

```python
text = "red,green,blue"

words = text.split(",")
result = "|".join(words)
```

---

## Q7 — List Mutation (3 marks)

Determine the final output:

```python
values = [3, 5, 7]

values.append(9)
values[1] = values[0] + values[2]

print(values)
```

Then answer:

> What is the difference between `values.append(9)` and `values[1] = ...`?

---

# Part B — Programming Challenges (15 marks)

## Q8 — String Challenge (3.75 marks)

Write:

```python
def extract_digits(text):
    ...
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
    ...
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
    ...
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
def count_words_starting_with(words, letter):
    ...
```

Return how many words in the list start with `letter`, ignoring capitalization.

Example:

```python
words = ["Apple", "ant", "Banana", "apricot", "pear"]

count_words_starting_with(words, "a")
→ 3
```

Your function should work with an empty list.

