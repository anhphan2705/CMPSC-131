numbers = input("Enter the numbers:") 
b = int(input("Enter b:"))
numbers=numbers.split()
i = 0
while i < len(numbers):
    numbers[i] = int(numbers[i])
    i += 1
    
Divisible_Numbers = []
Non_Divisible_Numbers = []
Divisible_Numbers_Index = 0
Non_Divisible_Numbers_Index = 0

i = 0
while i < len(numbers):
    if numbers[i] % b == 0:
        Divisible_Numbers.append(numbers[i])
        Divisible_Numbers.sort()
        Divisible_Numbers.reverse()
    else:
        Non_Divisible_Numbers.append(numbers[i])
        Non_Divisible_Numbers.sort()
    i += 1

i = 0
while i < len(numbers):
    if numbers[i] % b == 0:
        numbers.insert(i, Divisible_Numbers[Divisible_Numbers_Index])
        numbers.pop(i + 1)
        Divisible_Numbers_Index += 1
    else:
        numbers.insert(i, Non_Divisible_Numbers[Non_Divisible_Numbers_Index])
        numbers.pop(i + 1)
        Non_Divisible_Numbers_Index += 1
    i += 1
        
print("The sorted sequence is:", end ="")
i = 0
while i < len(numbers):
    print(numbers[i], end = " ")
    i += 1
