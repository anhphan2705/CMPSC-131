user_input = int(input("Please enter n: "))

##Starting Larger Prime Process##

#Initializing
print("Larger primes:", end=" ")
prime = user_input
prime_no = 0

#Checking if prime is valid
if (prime < 3):
    is_unvalid_prime = True
else: 
    is_unvalid_prime = False

#Finding 5 prime numbers
while ((prime_no < 5) and (not is_unvalid_prime)):
    prime +=1
    divider = 2
    is_prime = True

    while ((divider <= (prime/2)) and (is_prime)):
        if prime % divider == 0:
            is_prime = False
        divider += 1
    #Printing prime
    if (is_prime):
        print(prime, end=" ")
        prime_no += 1

##Starting Smaller Prime Process##

#Initializing
print()
print("Smaller primes:", end=" ")
prime_no = 0
prime = user_input

#Finding 5 prime numbers
while ((prime_no < 5) and (not is_unvalid_prime)):
    prime -=1
    divider = 2
    is_prime = True

    if (prime < 3):
        is_unvalid_prime = True
    
    while ((divider <= (prime/2)) and (is_prime)):
        if prime % divider == 0:
            is_prime = False
        divider += 1
    #Printing prime
    if (is_prime):
        print(prime, end=" ")
        prime_no += 1
        


