#Part 1
def average_speed(_distance1, _time1, _distance2, _time2):
    d_total = distance1 + distance2
    d_time = time1 + time2
    vavg = d_total/d_time
    return vavg

# distance1 = int(input("Enter first distance(km): "))
# time1 = int(input("Enter first travel time(hours): "))
# distance2 = int(input("Enter second distance(hours): "))
# time2 = int(input("Enter second travel time(hours): "))
# print(average_speed(distance1, time1, distance2, time2))

#Part 2
def student_result(midterm, final_exam):
    finalGrade= midterm * 0.40 + final_exam * 0.60
    if(finalGrade >= 80): return "Excellent"
    elif(finalGrade >= 60): return "pass"
    else: return "fail"

# midterm = int(input("Enter midterm grade: "))
# final_exam = int(input("Enter final exam grade: "))
# print("Result:", student_result(midterm, final_exam))

#Part 3 - Number Processing
def calculatesum():
    total = 0
    count = 0
    for i in range(6):
        number = int(input(f"Enter number{i+1}: "))
        if(number%2 == 0): total += number/2
        else: total += number*2
        if(number%3 == 0): count += 1
        i+=1
    return total, count

# print(calculatesum())

#Part 4 - Middle Cross Pattern (9 marks)
"""
Write a Python program that asks the user to enter a positive odd integer n.
Using nested loops, display the pattern shown below.
Enter a positive odd integer: 5
- - + - -
- - + - -
+ + + + +
- - + - -
- - + - -
"""
def drawCross(oddInteger):
    result = ""
    #Nested loop
    for i in range(oddInteger): 
        for j in range(oddInteger):
            if(i == oddInteger//2 or j == oddInteger//2):
                result += "+ "
            else:
                result += "- "
        result += "\n"
        i+=1
        j+=1
    return result
        

number = int(input("enter positive odd integer: "))
print(drawCross(number))