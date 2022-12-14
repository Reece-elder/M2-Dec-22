# Files of multiple types can be read and accessed by Python
colours_file = open("colours.txt")
print(colours_file)

data = colours_file.readline() # readline returns the first line of the file

print(data)
colours_list = data.split(",") # Converting string to a list
print(colours_list)

for line in colours_list:
    print(line)

# Once you have finished working on a file to close it
colours_file.close()


# With command, lets us directly open and access a file with it closing automatically
# r - read
# w - write  (clear the file and add new text)
# a - append (add the new text to the end)
with open("colours.txt", "r") as file:
    for line in file:
        print(line)

colour = "red"
new_line = True

with open("newfile.txt", "a") as new_file:
    new_file.write("Text\n")  # \n new line
    new_file.write("Hello!\n")
    new_file.write("new text..\n")
    if new_line:
        new_file.write(f"Colour is {colour}\n")

words = ["apple", "bus", "bottle", "cabbage"]

# with open("commaFile.txt", "w") as comma_file:
#     for word in words:
#         comma_file.write(f"{word},\n")

with open("commaFile.txt", "r") as read_file:
    content = read_file.readlines()
    print(content)
