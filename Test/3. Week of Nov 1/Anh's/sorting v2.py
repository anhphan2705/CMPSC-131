#Ask user for needed information & initializing variables/lists
numbers = str(input("Enter the numbers: "))
number_list = numbers.split(' ')
b = int(input("Enter b: "))

divisible = []
not_divisible = []
divisible_index = []
not_divisible_index = []

#Initialize list function
def list_initializer(length):
    return [None] * length

#Appending value function
def append_value(index, list, index_list):
    list.append(int(number_list[index]))
    index_list.append(index)

#Assigning value function
def assign_value(position, list, index_list, index_position = 0):
    for index in index_list:
        if (position == index):
            result_list[position] = list[index_position]
            list.pop(index_position)

#Print result function
def print_result(result):
    print("The sorted sequence is:", end=" ")
    for num in result:
        print(num, end=" ")

## main

#Creating the result list
result_list = list_initializer(len(number_list))

#Adding values into appropriate list by divisible by b or not
for pos in range(0, len(number_list)):
    if (int(number_list[pos]) % b == 0):
        append_value(pos, divisible, divisible_index)
    else: 
        append_value(pos, not_divisible, not_divisible_index)
 
#Sorting value in the list
divisible.sort(reverse=True)
not_divisible.sort()

#Assigning value for the result
for pos in range(0, len(number_list)):
    assign_value(pos,divisible, divisible_index)
    assign_value(pos,not_divisible, not_divisible_index)

#Print result
print_result(result_list)