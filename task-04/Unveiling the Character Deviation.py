t = int(input())
for j in range(t):
    substr = input()  
    refstr= "amfoss"  
    substr=substr[:len(refstr)]
    count= 0  
    
    for i in range(len(substr)):
        if substr[i] != refstr[i]:
            count += 1

    print(count)  
