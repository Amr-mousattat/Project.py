total = 0

for i in range(1, 5):
    total += i

print(total) # prediction 1+2+3+4 = 10 

#challenge one loop returning 0,1,2,3,4

for i in range(5):
    print(i) # prediction 0,1,2,3,4

# Challenge two loop returning 3,4,5,6,7

for i in range(3,8):
    print(i) # prediction 3,4,5,6,7

#Challenge three loop returning 2,4,6,8,10

# this range type gives the start number (2 in this case), the end number (11 in this case since we want to include 10)
# and the step (2 in this case since we want to increment by 2 each time).
for i in range(2,11,2):
    print(i) # prediction 2,4,6,8,10


# Part 3 - Trace an Accumulator 

# total = 0

# # 1 + 2 + 3 + 4 + 5 = 15
for i in range(1, 6):
    total += i

print(total)

# # Modify make it give 2+4+6+8+10 = 30
total = 0
for i in range(2,11,2):
    total += i

print(total) # prediction 30

# #Part 4 - Lopp through Each Item 

measurements = [12.1, 11.8, 12.5]

for measurement in measurements:
    print(measurement)

# what will be printed is the three values in the list, one per line:
# 12.1
# 11.8
# 12.5

measurements = [12.1, 11.8, 12.5]

for measurement in measurements:
    print(f"{measurement} units") # prediction 12.1 units, 11.8 units, 12.5 units


# Why is for measurement in measurements: a better choice than an index when you don't need the position
# because it's more readable and less error-prone

# Part 5 - While loops and the Progress Variable
time = 0

while time <= 10:
    print(time)
    time += 1

# 11 values will be printed from 0 to 10 inclusive 
# What is the progress variable? 
# The progress variable is the variable that controls the loop's execution and determines when the loop will terminate. 
# In this case, the progress variable is `time`, which is incremented by 1 in each iteration of the loop until it exceeds 10,
# at which point the loop stops.

# Part 6 - Debugging a infinite loop
x = 0

# while x < 10:
#     print(x)

# Will this loop stop? No, this loop will not stop because the value of x is never updated within the loop. So add += 1 to x to fix this issue 
# so that the loop will eventually terminate when x reaches 10.

# Part 7 Break and Continue

# This program will print the values in the list until it encounters a negative value, at which point it will skip that value 
# and continue with the next iteration of the loop. If it encounters a zero, it will break out of the loop completely.
values = [3, -1, 5, 0, 8]

for value in values:
    if value < 0:
        continue

    if value == 0:
        break # loop is stopped completely 

    print(value)

# Part 8 - Function modified: ignores negative values and stops at zero
values = [3, -1, 5, 0, 8]

for value in values:
    if value < 0:
        continue

    if value == 0:
        break

    #now we would like to sum up the positive values before the zero \
    total += value
    print(total) # prediction 3, 8

# Part 9 - Scientific Sampling
time = 0

while time <= 5:
    height = 100 - 4.9 * time ** 2
    print(time, height)
    time += 0.25

"""
Sampling Interval: 0.5 second 
Variable controlling termnination: time <= 5
Variable calculated each time: height
"""

# Part 10 - Floating Point Loop warning 
# x = 0.0

# while x != 1.0:
#     x += 0.1


#Should this loop reach exactly 1.0? Yes, other wise it will not even stop

for step in range(11):
    x = step * 0.1
    print(x)

#Why a counter is better? less likely to do mistake where the code would end up stuck in either the 
# the for loop or the while loop; a range would guarantee the code stopping at some point knowing that 
# x is getting implemented 

# Part 11 -
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]
size = 0
total = 0

for measurement in measurements:
    if(measurement < 0):
        continue
    if(measurement == 0):
        break
    
    total += measurement
    size += 1

print(f"size: {size}_total sum: {total}")

# Part 12 
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]

largest = 0
for meaasurement in measurements:
    if(largest <= meaasurement):
        largest = meaasurement


print(f"the largest is {largest}")

# part 13 - debugging code
# what the programmer wants to do is sum up all the numbers > 0 and before finding a 0 
# however the student miswput the break and continue (putting the continue on 0) and stopping the code as soon as a negative 
# value is read by the loop 

measurements = [12.4, -1.0, 13.2, 0.0, 14.1]

total = 0

for measurement in measurements:
    if measurement < 0:
        break

    if measurement == 0:
        continue

    total += measurement

print(total)

# Final reflection - 
"""
1
When is for loop a natural choice?

When is a while a natureal choice?
2
3
4
"""