# this function prints "Hello, World!" to the console
def hello_world():
    print("Hello, World!")

# this function takes user input for name, age, and height, and prints a greeting message
def input_outputf():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))


    print(f"Hello, {name}!")
    print(f"You are {age} years old.")
    print(f"Your height is {height} meters.")
    print(f"You will be " + str(age + 6) + " years old in 6 years.")
    # the str(age + 6) converts the integer value of age + 6 into a string so 
    # that it can be linked with the rest of the string of the print statement while also adding 6 to the age value.

hello_world()
input_outputf()