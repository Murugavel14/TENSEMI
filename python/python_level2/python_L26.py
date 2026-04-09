def main():
    count = 0
    for i in range(59,100000):
        div = 0
        sum = 0
        temp = i
        while (temp > 0):
            div  = temp % 10	
            temp //= 10	
            # print(div, temp)
            sum = sum + div 	#(0 + 6 )  6
            # print("sum -->",sum)
        if(sum == 14):
                count = count + 1
                print("count -->",count)
                print("14 -->",i)
    add = count
    print(f"Result = {add}") 
if __name__ == "__main__":
    main()
#---- ALTERNATE MEDHOD ---
	Simple ah um pannalam like ithu 6 digit ah so athunala 6 digit ah maddum
	Simple ah variable la declare pannitu poitalam but not efficiency.
