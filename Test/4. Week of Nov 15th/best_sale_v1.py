file = open("info.txt")
file2 = open("sales.txt")
lst1 = []
lst2 = []

for i in file:
    lst1.append(str(i.strip()))
for i in file2:
    lst2.append(str(i.strip()))
    
highest = 0
month = int(input("Please enter the desire month "))
money = 1

for i in lst2:
    if int(i[14:16]) == month:
        money = float(i[4:10])
    if money >highest and int(i[14:16]) == month:
        highest = money
        highest1 = int(i[0:3])
        
person = 0
name = ""
for i in lst1:
    person = int(i[len(i)-3:len(i)])
    if person == highest1:
        name = i[:len(i)-4]
        
print("The higest sales for month ", month, " was made by", name)