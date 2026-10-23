"""
For every question:

implement the function;
explain inputs, outputs, and algorithm;
include normal and boundary cases;
write automated tests;
be prepared for a short code-verification modification.
"""


# Q1 — Remove Duplicates and Sort
"""Return a sorted list containing each value once.

Example:

[4, 2, 4, 1, 2] → [1, 2, 4]
"""
def unique_sorted(numbers : list):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result.sort()

"""
Q2 — Cumulative Sum
Return a new list.

Example:

[2, 3, 5] → [2, 5, 10]
"""

def cumulative_sum(numbers : list):
    result = []
    sum = 0
    for num in numbers:
        sum += num
        result.append(sum)

    return result

"""
Q3 — Every Nth Element
Return every nth element.

Define and document what happens when:

n <= 0 
-> if number is exactly equal to 0; a valueError would be returned since slice step cannot be equal to zero,
-> otherwise it would return the last value of the list, or values[-1]
n > len(values) -> if values is bigger than len(values), it would simply return the first value (so values[0]) or nothing if list is empty

"""
def every_nth(values : list, n):
    if(n<= 0):
        return ValueError("number must be more than 0")
    else:
        listy = values[::n]

    return listy

# value = [1,2,3,4,5]

# print(every_nth(value, n = 0))

"""
Q4 — Dot Product
"""

def dot_product(a : list, b : list):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

# print(dot_product(a=[1,2,3] , b = [4,5,6])) #expected: 32

"""
Q5 — Matrix Multiplication
The number of columns in A must equal the number of rows in B.

Example:

A = 2*3
B = 3*2
result = 2*2 -> basically a square if you think about it
"""

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal the number of rows in B.")
    rows_A = len(A)
    rows_B = len(B)
    col_B = len(B[0])

    result = []

    for i in range(rows_A):
        new_row = []
        for j in range(col_B):
            product = sum(A[i][k] * B[k][j] for k in range(rows_B))
            new_row.append(product)
        result.append(new_row)

    return result

A = [[1, 2, 3],
     [4, 5, 6]]  # 2x3 matrix

B = [[7, 8],
     [9, 1],
     [2, 3]]  # 3x2 matrix

print(matrix_multiply(A, B))