def get_road(quantity):
    
    road_list = []
    for i in range(quantity):
        road = input("Enter road: ")
        road_list.append(road.split("-"))
        
    return road_list

def find_way(departure, destination, road_list, trip):
    starting = departure
    ending = destination
    start_road = []
    end_road = []
    
    if len(trip) > 0:
        for road in trip:
            if road in road_list:
                road_list.remove(road)
            else: 
                return []

    for row in range(len(road_list)):
        for column in range(len(road_list[row])):
            
            if road_list[row][column] == departure:
                start_road = road_list[row]
                starting = road_list[row][abs(column-1)]
                trip.append(road_list[row])

            if road_list[row][column] == destination:
                end_road = road_list[row]
                ending = road_list[row][abs(column-1)]
                trip.append(road_list[row])
    
    if starting == ending:
        return trip
    elif start_road == end_road:
        trip.pop()
        return trip
    else:
        return find_way(starting, ending, road_list, trip)
    
def result(predicted_journey):
    if len(predicted_journey) <= 4 and len(predicted_journey) != 0:
        print("Yes it is posibble to go from the starting city to the destination city using 4 or fewer roads")
    else:
        print("No it is not possible to go from the starting city to the destination city using 4 or fewer roads")
        
def main():
   num_road = int(input("Please enter the number of road: ")) 
   road_list = get_road(num_road)
   departure_city = input("Enter starting city: ")
   arrival_city = input("Enter destination city: ")
   journey = find_way(departure_city, arrival_city, road_list, [])
   print(f"The road you have to use are {journey}")
   result(journey)
   
main()