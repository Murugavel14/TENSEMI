def main():
    char     = input("Enter string : ")
    sub_char = input("Enter Sub str: ")
    char_arr = [0] * (len(char))
    length   = len(sub_char)
    count    = 1
    for i in range(1,(len(char)),1):
        count += 1
        if ((char[i:i + length]) == sub_char):
            break
            # break
    print(f"Result = {count}")
if __name__ == "__main__":
    main()
# ----- ALTERNATE -------
    char     = input("Enter string : ")
    sub_char = input("Enter Sub str: ")
    fin_d    = char.find(sub_char)
    print("Position", fin_d + 1)
# -------- XXXXX -----------
