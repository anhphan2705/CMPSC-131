user = str(input("Please enter the booster times"))
rest = int(input("Please enter wanted break time"))
midnight = 0
lst = [user.split()]
minutes = []
possible = True
for i in lst:
    for time in i:
        if time[-2:] == "PM":
            if time[1] == ":":
                midnight = 720 + (60 * int(time[0])) + (10 * int(time[2])) + int(time[3])
            elif time[:2] == "12":
                midnight = 720 + (10 * int(time[3]) + int(time[4]))
            elif time[2] == ":":
                midnight = 720 + (60 * int(time[:2])) + (10 * int(time[3])) + int(time[4])
        elif time[-2:] == "AM":
            if time[1] == ":":
                midnight = (60 * int(time[0])) + (10 * int(time[2])) + int(time[3])
            elif time[:2] == "12":
                midnight = (10 * int(time[3])) + int(time[4])
            elif time[2] == ":":
                midnight = (60 * int(time[:2])) + (10 * int(time[3])) + int(time[4])
        minutes.append(midnight)
minutes.sort()

for i in range(0, len(minutes) - 1):
    if possible:
        if minutes[i + 1] - minutes[i] < rest + 5:
            possible = False

if possible:
    print("Break possible")
else:
    print("Break not possible")