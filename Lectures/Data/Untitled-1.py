with open("Lectures/Data/sample_text.txt", "r") as file:
    for line in file:
        print(line.strip())
        file = open("sample_text.txt", "r")

content = file.read()
print(content)

file.close()



