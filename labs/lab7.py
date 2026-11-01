"""
d1 = last digit
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
"""
studentID = str(input("Input your student ID: "))
d1 = int(studentID[-1])
if(len(studentID) >= 2): d2 = int(studentID[-2])
else : d2 = 0
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2

#Part A — Dimensions and structure
"""
Use either:

2 rows × 5 columns, or
4 rows × 3 columns.
Print:

number of rows;
number of columns;
every row separately;
last column;
first three columns of every row.
Important
Do not assume:

len(matrix) == len(matrix[0])
That would be true only for a square matrix.
"""

matrix = [[1,2,3,4,5],
          [6,7,8,9,10]]
print("number of rows:", len(matrix))
print("number of columns:", len(matrix[0]))

#each row printed individually
rows_printed = "number of rows:\n"
for row_index in matrix:
    rows_printed += str(row_index) 
    rows_printed += "\n"
print(rows_printed)

#Part B — ID-selected row

row_index = d1 % len(matrix)

oldRow = matrix[row_index]
newRow = [value + k for value in oldRow]

print("index", row_index)
print("Old row:", oldRow)
print("New Row:", newRow)
sidebySide = "rows sidebySide\n" + str(oldRow) + "->" + str(newRow)
print(sidebySide)

#Part C — Slicing challenge
start_column = d2 % 2

for row in matrix:
    print(row[start_column:])

"""
Explain the difference between:

row[start_column:] -> This operates on one row, and removes the start column
and:

matrix[start_column:] -> this operates on the outer list, I.E instead of removing the start column,
it would rather remove a whole row.
"""

#Part D — Debugging
"""
Find the error:

for column in range(len(matrix)):
    print(matrix[0][column])
This code is not necessarily safe for a rectangular matrix.

Explain why.
 - the reason why this code isn't necessarily safe a for a rectangular matrix since the len(matrix) returns the length of rows and 
 NOT the length of columns present; this would be unsafe for a general rectangle since the number of rows and columns may be different 
Rewrite it to extract the first row correctly.
CORRECT VERSION:

for column in range(len(matrix[0])):
    print(matrix[0][column])
This code is not necessarily safe for a rectangular matrix.
"""

#Part E — Design challenge
"""
returns (rows, columns)
"""
def dimensions(matrix: list):
    return len(matrix), len(matrix[0])

print("Maxtrix dimensions:",dimensions(matrix))

def last_column(matrix: list):
    last_column = []
    for row in matrix:
        last_column.append(row[-1])

    return last_column
print("last_columns",last_column(matrix=matrix))