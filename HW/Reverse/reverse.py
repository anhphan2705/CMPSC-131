num = int(input("Please enter a 4 digits number: "))

a = int(num/1000)
b = int(num%1000/100)
c = int(num%100/10)
d = int(num%10)

print("The number in reverse is", d*1000+c*100+b*10+a)
