numbers=[-32,200,20,3,11,34,12,3]
for i in range(1,len(numbers)):
    temp=numbers[i]
    step=i-1
    counter=0
    while temp<numbers[step]:
        numbers[step+1]=numbers[step]
        step=step-1
        counter+=1
    print (counter)
    numbers[step+1]=temp
    print (numbers)