def main():
    char = input("Enter string : ")
    result = [0] * (len(char))
    result = char
    count  = 1
    find   = input("Enter the char: ")
    for i in char:
        if ( i == find):
            print(count)
        count += 1
    print(f"Result = {result}")
if __name__ == "__main__":
    main()
