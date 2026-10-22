"""
d1 = last digit of student ID
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2
"""
studentID = str(input("Input your student ID: "))
d1 = int(studentID[-1])
d2 = int(studentID[-2])
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2


# Part A - Explore the grid
matrix = [[0,1,2,3],
          [4,5,6,7],
          [8,9,10,11]]

for row in matrix:
    print(row) # print entire matrix row by row

#one specified element
print(matrix[1][2]) # expected: 6

# two rows
for row in matrix[:2]:
    print(row) 

# first column
firstColumn = [row[0] for row in matrix]
print(firstColumn)

# Upper left 2x2 sub-array
upper_left_2x2 = [row[:2] for row in matrix[:2]]

for row in upper_left_2x2:
    print(row)

#Part B
row_index = d1 % len(matrix)

initMatrix = [row for row in matrix]
oldRow = list(matrix[row_index])


newRow = [val + shift for val in oldRow]
matrix[row_index] = newRow

print("index", row_index)
print("old row:", oldRow)
print("new row:", newRow)
print("before")
for row in initMatrix:
    print(row)

print("after")
for row in matrix:
    print(row)

#Part C — Personalize one column
column_index = d2 % len(matrix[0])

initColumn = [row[column_index] for row in matrix]

for row in matrix:
  row[column_index] *= k

finalColumn = [row[column_index] for row in matrix]

print("Part C: ")
print("Column Index:", column_index)
print("Multiplier k:", k)
print("Old Column:", initColumn)
print("New Column:", finalColumn)

#Part D — Sub-array
#Do not assume k is smaller than the number of columns; handle the situation safely.
sub_array = [row[:k] for row in matrix[:rows_keep]]
print("Sub-array:", sub_array)
"""
grid = [[1, 2], [3, 4]]
copy_grid = grid[:]

copy_grid[0][0] = 99

print(grid)
"""
#tExplain why slicing the outer list does not create independent inner lists.
"""
Python creates a brand-new outer list container, but it does not duplicate the objects stored inside of it.
The outer list would be held in memory and will have a new memory, but not the inner list which will 
always keep the same memory as the one associated to the old array
 """