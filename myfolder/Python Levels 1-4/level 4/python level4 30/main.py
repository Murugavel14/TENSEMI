for i in range(99999999,9999999,-1):
    count=0
    for j in range(1,((i+1)//2)+1):
        if(i%j==0):
            count+=1
    if(count==1):
        print(i)
        break
            