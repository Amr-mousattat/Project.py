a = [10, 20, 30]
b = [1, 2, 3]
"""
zip(a, b): Pairs the elements from both lists index by index, creating pairs of tuples: (10, 1), (20, 2), and (30, 3).

for x, y in ...: Unpacks each tuple as it loops—x takes the value from list a, and y takes the value from list b.

x + y: Adds them together element-wise (10 + 1, 20 + 2, 30 + 3).

[...]: The list comprehension collects the results into a brand new list.
"""
result = [x + y for x, y in zip(a, b)]
print(result)

# debugging 
readings = [10, 20, 30]
shift = 10
shifted = readings

# for i in range(len(readings)):
#     shifted[i] += shift
"""
Why does this not work?
because shifting = readings does not create a brand-new list. Instead it creates a new 
variable named shifted that point to the exact same list object in memory as readings 

What to do instead?
shifted = readings.copy or readings[:] or list(readings) or a for loop
"""
#way #4
shifted = [x + shift for x in readings]

#way #5
for i in readings:
    shifted.append(readings+shifted)

def calibrate(readings, shift, k):
    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]
    combined = [x + y for x,y in zip(readings,shifted)]
    return shifted, scaled, combined

original, hShift, kScale = calibrate(readings, shift, 10)
print("Shifted:", hShift)
print("Scaled:", kScale)
print("Combined:", original)

measurements = [12.4, -1.0, 13.2, 0.0, 14.1]

def calculateList(measurements: list):
    size = 0
    total = 0
    for x in measurements:
        if(x < 0): continue
        if(x == 0): break
        size += 1
        total += x
    return size, total

size, total = calculateList(measurements=measurements)
print("size", size)
print("total", total)