"""
1. what does each function receive?
calculate_height(h0, t) receives the initial height h0 in meters and time t in seconds as inputs.
calculate_car_distance(t) receives time t in seconds as input.
2. What should each function return?
calculate_height(h0, t) should return the height of the ball (in meters) at time t.
calculate_car_distance(t) should return the distance traveled by the car in meters.
3. write a short algorithm;
4. What constant is needed for the falling-ball problem?
we need the gravity constant which is g = 9.8 m/s^2
5. What examples in the test file give you expected results?
calculate_height(50, 1) -> 45.1
calculate_height(50, 2) -> 30.4
calculate_height(50, 3)  ->5.9
calculate_car_distance(1) -> 20
calculate_car_distance(2) -> 40
calculate_car_distance(3) -> 60

6.What edge case is explicitly tested?
t = 0 for the falling ball (should return h0)
t = 0 for the car (should return 0)
"""

# Part 1 - Falling Ball: algorithm first 

# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    ht = h0 - 0.5 * 9.81 * t**2  # Using the formula h = h0 - (1/2)gt^2
    # if we put t*2 instead of t**2, it would be incorrect because the formula for the height of a falling object under gravity 
    # is h0 - (1/2)gt^2, where t is squared to account for the acceleration due to gravity over time. By doing t * 2, we would be multiplying and not squaring the time
    return ht

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
# input : t (time in seconds)
# Constant: speed = 20 m/s
# output: distance traveled by the car in meters
# units: meters
def calculate_car_distance(t):
    speed = 20 # speed of the car in meters per second
    d = speed * t # Using the formula d = speed * time to have the distance in meters
    return d

ho = int(input("Enter initial height: "))
t = int(input("Enter time: "))
height = calculate_height(ho, t)
print(f"Height of the ball at time {t} seconds = {height} meters.")

time_car = int(input("Enter time for car distance calculation: "))
car_distance = calculate_car_distance(time_car)
print(f"The car will travel {car_distance} meters in {time_car} seconds.")

# Part 3 - predict before running 
print(calculate_car_distance(3))  # Expected output: 60 -> that was correct :)

# Part 4 - Debugging code
# print(calculate_height(50, 0))  # Expected output: 50 
# print(calculate_height(50, 1))  # Expected output: 45.095

# correct version
# def calculate_height(h0, t):
#     ht = h0 - 0.5 * 9.81 * t**2  # Using the formula h = h0 - (1/2)gt^2
#     # if we put t*2 instead of t**2, it would be incorrect because the formula for the height of a falling object under gravity 
#     # is h0 - (1/2)gt^2, where t is squared to account for the acceleration due to gravity over time. By doing t * 2, we would be multiplying and not squaring the time
#     return ht
# # incorrect version
# def calculate_height(h0, t):
#     ht = h0 - 0.5 * 9.81 * t*2  # Using the formula h = h0 - (1/2)gt^2
#     return ht

"""
1. What is different?
Correct version uses t**2 (t^2 or t squared) while the incorrect version uses t*2 (2t).

2. why does ** 2 matter?
The ** operator is required in this case for the physics formula : h = h0 - (1/2)gt^2, where t is squared to account for the acceleration due to gravity over time. 
By doing t * 2, we would be multiplying and not squaring the time, which would lead to incorrect results.

3. What result would the second version give for (50, 2)?
2nd version would give 50 - 0.5 * 9.81 * 2*2 = 50 - 19.62 = 30.38, which is incorrect because it does not follow the correct physics formula for free fall.

4. How would you detect the error by tracing rather guessing?
by unit testing the function with known values and comparing the outputs to the expected results based on the correct formula. 


"""

# Part 5 - Scientific Model Challenge
# calculate_height(50, 4) #Answer: -29.2 meters. The height is negative because the ball has fallen below the 
#                                initial height of 50 meters after 4 seconds, indicating it has hit the ground and continued to fall.
"""
Is the Python calculation wrong, or might the physical model have reached its domain limit?
the python calculation is correct based on the formula used, but the physical model has reached its domain limit. 
The formula assumes free fall under gravity without any constraints, 
so when the calculated height becomes negative, it indicates that the ball has fallen 
below the initial height and would have hit the ground. In reality, once the ball hits the ground, 
it cannot go below that point, so the model's assumptions no longer hold true beyond that point.
"""

# Part 6 - Extension challenge
def calculate_car_average_speed(d, t):

    """"
    
    """
    average_speed = d / t  # Average speed formula: distance / time
    if t == 0:
            return 0  # Avoid division by zero
    else:
        return average_speed

# Part 7 - Explain the code
# function chosen: calculate_height(h0, t)
# Q: What are its inputs?
# A: h0 (initial height in meters) and t (time in seconds)
# 
# Q: what does it return?
# A: height of the ball h(t) at time t in meters.
# 
# Q: What formula does it implement?
# A: h(t) = h0 - 0.5 * g * t^2, with g = 9.8 m/s^2.
#
# Q: What assumption does the formula make?
# A: The ball is in free fall under constant gravity and the height can reach negative values 
#
# Q: What is the one edge case?
# A: When t = 0, the height is equal to the initial height h0.
#
# Q: Which test gives you the most confidence and why?
# A:  calculate_height(50, 2) == 30.4 because it matches the expected value calculated manually using the formula, 
# confirming the function's correctness for a typical case.
#
