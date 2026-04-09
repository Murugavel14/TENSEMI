def main():
    x = int(input("Enter Number: "))
    count = len(str(x))
    digit = count - 1
    last = x // (10 ** digit)
    div = x % (10 ** digit)
    if ((last % 2) != 0):
        last = last - 1
    y = (last * (10 ** digit)) + div
    print(f"Result = {y:0{count}d}") 
 # Ithukku peru formatting,  y  actual output 
#(:0{count}d)   ({count}d)  Dynamic width nu solluthu , d  intiger nu solluthu 
#(:0{count}d)   :0   ithukku peru “padding” fixed la output varalana 0 add pannum
if __name__ == "__main__":
    main()

