def main():
    result = 0
    for i in range(11,100,2):
        first  = (i // 10)
        second = (i % 10)
        sum    = (first + second)
        if(sum == 7):
            print(i)
if __name__ == "__main__":
    main()
# ------ ALTERNATE METHOD HERE ----
def main(): 
	for i in range(11, 100, 2):
		 if (i // 10 + i % 10) == 7: 
			print(i) 
if __name__ == "__main__": 
	main() 
