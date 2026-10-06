

"""
d1 = last digit of student ID
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
"""
d1 = int(input("Enter your last digit of the student ID: "))
d2 = int(input("Enter your second last digit of your student ID: "))

k = (d1 + d2) % 4 +2
shift = d1 - d2

print("d1", d1)
print("d2", d2)
print("k", k)
print("shift", shift)



# Part A - Measurement List
count = int(input("how many readings: "))
readings = []

for i in range(count):
    readings.append(int(input(f"Enter reading {i+1}: ")))

if readings:
    print("Readings: ", readings)

#to check if list isn't empty
if readings:
    print("Reading 1:", readings[0])
    print("Last reading:", readings[-1])
    if len(readings) >= 4: print("slice:", readings[1:4])
    else: print("Slice: list is too short")
    print("sum:", sum(readings))
else: 
    print("nothing inside list to begin with")

# Part B = Transform without destroying original
def measurement(reading, k, shift):
    shifted = [x + shift for x in reading]
    scaled = [x * k for x in reading]

    return shifted, scaled

shiftedRange = [x + shift for x in readings]
ScaledRange = [x * k for x in readings]
if readings:
    print("original ", readings)
    print("shifted:", shiftedRange)
    print("Scaled: ", ScaledRange)

# Part C - zip

zipped = [x + y for x,y in zip(readings, shiftedRange)]
if readings:
    print("zipped", zipped)

# Part D - Debugging

# readings = [10, 20, 30]
# shifted = readings

# for i in range(len(readings)):
#     shifted[i] += shift
# In this case all we are doing was give shifted the same memory as readings (meaning we did not make a copy with a shift added 

# way #1
readings = [10, 20, 30]
shifted = [x + shift for x in readings]

# way #2
readings = [10, 20, 30]
shifted = []

for i in range(len(readings)):
    shifted.append(i+shift)

# Part E - challenge
def calibrate(readings, shift, k):
    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]
    combined = [x + y for x,y in zip(readings, shifted)]

    return shifted, scaled, combined

shifted, scaled, combined = calibrate(readings, shift, k)

print("Shifted:", shifted)
print("Scaled:", scaled)
print("Combined:", combined)


