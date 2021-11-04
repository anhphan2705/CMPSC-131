#Ask user for needed information & initializing variables/lists
numbers = str(input("Enter the numbers: "))
number_list = numbers.split(' ')
b = int(input("Enter b: "))

divisible = []
not_divisible = []
divisible_index = []
not_divisible_index = []

#Initialize result list
result = [None] * len(number_list)

#Adding values into appropriate list
for index in range(0, len(number_list)):
    if (int(number_list[index]) % b == 0):
        divisible.append(int(number_list[index]))
        divisible_index.append(index)
    else: 
        not_divisible.append(int(number_list[index]))
        not_divisible_index.append(index)

#Sorting value in the list
divisible.sort(reverse=True)
not_divisible.sort()

#Assigning value for the result
div_pos = 0
not_div_pos = 0
for pos in range(0, len(number_list)):
    for index in divisible_index:
        if (pos == index):
            result[pos] = divisible[div_pos]
            div_pos += 1
    for index in not_divisible_index:
        if (pos == index):
            result[pos] = not_divisible[not_div_pos]
            not_div_pos += 1

#Print result
print("The sorted sequence is:", end=" ")
for num in result:
    print(num, end=" ")
