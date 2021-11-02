string = input("Please enter the string: ")
max = 1
max_char = ''

count = 1
char = ''
for i in range(1, len(string)+1):
    char = string[(i-1):(i)]
    next_char = string[(i):(i+1)]
    if (char == next_char):
        count += 1
        if (count > max):
            max = count
            max_char = char
    else:
        count = 1
print("The longest sequence is " + str(max_char) + " repeated " + str(max) + " times")


