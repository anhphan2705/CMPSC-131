# i = 0
# while(i < 50):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): 
#             break
#         j = j + 1
#         if (j > i/j): 
#             print(i, " is prime")
#     i = i + 1

# for num in range(2,101):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#     if prime:
#        print (num)

# num = int(input("Enter a number ( greater than 1)"))
# f = 0
# i = 2
# while i <= num / 2:
#     if num % i == 0:
#         f=1
#         break
#     i=i+1
    
# if f==0:
#     print("The entered number is a PRIME number")
# else:
#     print("The entered number is not a PRIME number")

# prime = 2
# while(prime_no < 5):
#     division_num = 2
#     isValid = True
#     while(division_num <= (prime / division_num) and isValid):
#         if (prime % division_num == 0):
#             isValid = False
#         division_num += 1
#         if (division_num > (prime / division_num) and (prime > user_input) and isValid):
#             print(prime, end=" ")
#             prime_no += 1
#     prime += 1

# num = int(input("Enter a number: "))
# prime = num
# prime_no = 0

# while (prime_no) < 5:

#     prime +=1
#     divider = 2
#     is_prime = True

#     while ((divider <= (prime/2)) and (is_prime)):
#         if prime % divider == 0:
#             is_prime = False
#         divider += 1
        
#     if (is_prime):
#         print(prime)
#         prime_no += 1

n = int(input("Please enter n: ")) 

print("Larger primes:", end=" ")
prime_no = n
num_prime = 0

if (prime_no < 1):
    isprime = True
else:
    isprime = False

while (num_prime < 5):
    prime_no += 1
    d = 2
    is_prime = True

    while (d <= prime_no/2):
        if prime_no%d == 0:
            is_prime = False
        d += 1

    if(is_prime):
        print(prime_no, end=" ")
        num_prime += 1

print()
print("Smaller primes:", end= " ")
prime_no = n
num_prime = 0

while (num_prime < 5):
    prime_no -= 1
    d = 2
    isprime = True

    if (prime_no < 2):
        isprime = False
    while (d <= prime_no/2):
        if prime_no%d == 0:
            isprime = False
        d += 1

    if (isprime):
        print(prime_no, end= " ")
        num_prime += 1


    