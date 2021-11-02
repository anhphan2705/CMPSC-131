binary_num = int(input("Enter up to a 5 bit number: "))

fifth_digit = int(binary_num/10000)
forth_digit = int(binary_num%10000/1000)
third_digit = int(binary_num%1000/100)
second_digit = int(binary_num%100/10)
first_digit = int(binary_num%10)

if (len(str(binary_num)) > 5):
    print("Over 5 digits")
elif (fifth_digit != 1 and fifth_digit != 0) or (forth_digit != 1 and forth_digit != 0) or (third_digit != 1 and third_digit != 0) or (second_digit != 1 and second_digit != 0) or (first_digit != 1 and first_digit != 0):
    print("Not a valid binary number")
else:
    cnvrt_num = first_digit * (2**0) + second_digit * (2**1) + third_digit * (2**2) + forth_digit * (2**3) + fifth_digit * (2**4)
    print("The value in decimal is " + str(cnvrt_num))
