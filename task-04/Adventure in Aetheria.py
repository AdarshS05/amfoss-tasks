n = int(input())
time_to_cities= list(map(int,input().split()))

min_time=min(time_to_cities)
count= time_to_cities.count(min_time) 

if count == 1:
    town_num= time_to_cities.index(min_time) +1
    print(town_num)

if count>1:
    print("Still Aetheria")
    
