def day_type(day):
    if(1 <= day <= 5):
        return "Weekday"
    elif(day == 6 or day == 7):
        return "Weekend"
    else:
        return "Not a proper day number!"

def day_name(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if(1 <= day <= 7):
        return "it is a " + days[day - 1]
    else:
        return "Not a proper day number!"


print(day_type(1))  # Expected output: Weekday
print(day_name(4))  # Expected output: it is a Thursday
print(day_name(8))  # Expected output: Not a proper day number!

def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp < 20:
        return "Cold"
    elif 20 <= temp < 30:
        return "Moderate"
    else:
        return "Hot"

#Boundary test cases
# print(classify_temperature(-1))  # Expected output: Freezing
# print(classify_temperature(0))   # Expected output: Cold
# print(classify_temperature(19))  # Expected output: Cold
# print(classify_temperature(20))  # Expected output: Moderate
# print(classify_temperature(29))  # Expected output: Moderate
# print(classify_temperature(30))  # Expected output: Hot

#Part E - debegugging code
# def classify_temperature(temp):
#     if temp < 0:
#         return "Freezing"
#     elif temp < 20:
#         return "Cold"
#     elif temp < 30:
#         return "Hot"
#     elif temp >= 30:
#         return "Moderate"

# print(classify_temperature(-1))  # Expected output: Freezing
# print(classify_temperature(0))   # Expected output: Cold
# print(classify_temperature(19))  # Expected output: Cold
# print(classify_temperature(20))  # Expected output: Moderate
# print(classify_temperature(29))  # Expected output: Moderate -- answer received was hot 
# print(classify_temperature(30))  # Expected output: Hot answer -- received was moderate

"""
So what seems to be the issue the code above in part E?
The issue in the code above in part E is that the conditions for classifying the temperature are not correctly ordered, which leads to incorrect outputs for certain temperature ranges. Specifically:
1. The condition for "Hot" (temp < 30) is placed before the condition for "Moderate" (temp >= 30). 
This means that any temperature less than 30 will be classified as "hot" even if it should be classified as "Moderate" (20 <= temp < 30).
"""

# Part F - Explain
"""
function explained: day_name(day)
Validation condition: 1 <= day <= 7
Classification condition: Return the corresponding day name from the Array
First boundary value: 1
last boundary value: 7
one invalid input: 8
"""