numbers=[200,20,3,11,34,12,3]
for i in range (0,len(numbers)):
    counter=0
    for j in range(0,len(numbers)-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            counter+=1
            print(numbers)
    #print (counter)