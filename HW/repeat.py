user_string = input("Please enter the string: ")
max_repeat_count = 1
max_repeat_char = ''
current_count = 1
current_char = ''

def find_current_char(index):
    return user_string[(index - 1):(index)]

def find_next_char(index):
    return user_string[(index):(index + 1)]

def set_max(count, char):
    global max_repeat_count, max_repeat_char
    max_repeat_count = count
    max_repeat_char = char

def result(count, char):
    return f"The longest sequence is {char} repeated {count} times"


for char_index in range(1, len(user_string)+1):
    consc_char = find_next_char(char_index)
    current_char = find_current_char(char_index)
    
    if (current_char == consc_char):
        current_count += 1
        if (current_count > max_repeat_count):
            set_max(current_count, current_char)
    else:
        current_count = 1


print(result(max_repeat_count, max_repeat_char))


