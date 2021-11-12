#Initialize variables
boost_times = str(input("Please enter the boost time: "))
break_time = int(input("Please enter wanted break time: "))
boost_list = boost_times.split(" ")
boost_hour = []
boost_min = []
boost_time_minute = []
time_suffix = []
is_break = True

#Changing time into 24h clock
def change_24h(index):
    if (time_suffix[index] == "pm"):
        boost_hour[index] = boost_hour[index] + 12

#Changing time into minute only counting form 0 at 0:00am
def convert_to_minute(index):
    total_minute = boost_hour[index]*60 + boost_min[index]
    boost_time_minute.append(total_minute)

#Seperate time components
for time in boost_list:
    colon_pos = time.find(":")
    hour = int(time[:colon_pos])
    boost_hour.append(hour)
    min = int(time[(colon_pos+1):(colon_pos+3)])
    boost_min.append(min)
    suffix = time[-2:].lower()
    time_suffix.append(suffix)


for index in range(len(time_suffix)):
    change_24h(index)
    convert_to_minute(index)

boost_time_minute.sort()
    
#Adding monitor time into the boost time
for index in range(len(boost_list)):
    boost_time_minute[index] += 5

#Calculating availability for break
for index in range(1, len(boost_time_minute)):
    possible_break_time = boost_time_minute[index] - boost_time_minute[index-1]
    if (possible_break_time < break_time):
        is_break = False

#Print result
if is_break:
    print("Break possible")
else:
    print("Break not possible")