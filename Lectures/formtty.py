import datetime
my_date = datetime.datetime(2026, 10, 12, 3, 50, 50)

sentence = "{0: %B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence)


#Indexing --------
sentence = "This is a sentence"
index = sentence.index(" ")
print("index:", index)
print(sentence[:index-1])

def count_spacings(s: str):
    count = 0
    result = ""
    for a in s:
        if(a == " "): count += 1
        else: result += a.upper()

    return result, count
def count_spacings2(s: str):
    return f"{s.replace(" ", "")}\n{s.count(" ")}"

# print(count_spacings2("This is great!"))

s = "hello {}"
print(s.format("world"))
print(s.format("sonion"))

#numbers
# f stands for decimals
print("{:.7f}".format(0.667))
print("{:07.2f}".format(8))

print("{:#>5d}".format(5)) # to the left
print("{:#<5d}".format(5)) # to the right

def listyNummy(numbers: list):
    result = ""
    for number in numbers:
        result += "{:06.2f}".format(number)
        result += "\n"
    return result

print(listyNummy([10, 10.0, 1, 12.5]))

# join()

s = "happy,smiling,face"
words = s.split(",")
print(words)

result = ""
for word in words:
    result += word
    result += "\n"
print(result)



# Keep reading/storing input until a blank line.
food = []
while True:
    line = input("write down the food you want: ")
    if line == "":
        break
    food.append(line)

# Repeat back the order, separated by commas.
if len(food) == 0:
    print("You ordered nothing")
elif len(food) == 1:
    print("you ordered {food}".format(food=food[0]))
elif len(food) == 2:
    print("you ordered {0} and {1}".format(food[0], food[1]))
else:
    firstItems = ", ".join(food[:-1])
    print("you ordered {}, and {}.".format(firstItems, food[-1]))
