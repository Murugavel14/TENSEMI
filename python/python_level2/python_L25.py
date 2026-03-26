def main():
    count = 0 
    for i in range(9500,9999):
        if(i % 63 == 0):	#Why 63, because (7 x 9 = 63) so that’s it
            count = i
    print(count)
if __name__ == "__main__":
    main()

