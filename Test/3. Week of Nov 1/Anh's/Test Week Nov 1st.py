#Initialize variables
user_input = str(input("Enter the numbers: "))
user_input = user_input.split()
b = int(input("Enter b: "))

#Innitialize a new list function
def init_list(len):
    return [] * len

#Appending value to list function
def append_list(list, value):
    list.append(value)

#Assingign value to list function
def assign_list(list, list_index, value, value_index):
    append_list(list, value)
    list_index.append(value_index)

#Getting value from a list
def get_value(list, index):
    return list[index]

#Print result function
def print_result(result):
    print("The sorted sequence is", end=" ")
    for value in result:
        print(value, end=' ')

##Main##
mult_b = init_list(1)
mult_b_pos = init_list(1)
not_mult_b = init_list(1)
not_mult_b_pos = init_list(1)
result_list = init_list(len(user_input))

for index in range(0, len(user_input)):
    value = get_value(user_input, index)
    if (int(value) % b == 0):
        assign_list(mult_b, mult_b_pos, int(value), index)
    else:
        assign_list(not_mult_b, not_mult_b_pos, int(value), index)

mult_b.sort()
not_mult_b.sort(reverse=True)

for index in range(0, len(user_input)):
    for pos in mult_b_pos:
        if (index == pos):
            append_list(result_list, get_value(mult_b, 0))
            mult_b.pop(0)
    for pos in not_mult_b_pos:
        if (index == pos):
            append_list(result_list, get_value(not_mult_b, 0))
            not_mult_b.pop(0)

print_result(result_list)

        


