#Declare varibles
number_list = []
is_combination = False

#Ask user input
n = int(input("please enter n: "))
for question_no in range(n):
    number_list.append(int(input("please enter a number: ")))
k = int(input("please enter k: "))

#Finding the right combination by looping through all possible combinations of three number
test_list = number_list
for first_num in test_list: 
    test_list.remove(first_num)
    for second_num in test_list:
        test_list.remove(second_num)
        for third_num in test_list:
            sum = first_num + second_num + third_num
            if (sum == k):
                is_combination = True
        test_list.append(second_num)
    test_list.append(first_num)

#Print result
if is_combination:
    print("three numbers add up to k")
else: 
    print("no three number add up to k")

