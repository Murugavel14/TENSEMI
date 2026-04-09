def main():
    count = 0
    for i in range (0, 1001):
        temp = i
        if(temp == 0):
            count += 1
        else:
            while temp > 0:
                div  = temp % 10
                temp = temp // 10
                if(div == 0):
                    count += 1
                
    print(f"Result = {count}")
if __name__ == "__main__":
    main()
