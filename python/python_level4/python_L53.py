def main():
    sentance = input("Enter Number: ")
    word     = sentance.split() 
    print(f"Result = {len(word)}")
if __name__ == "__main__":
    main()

# ----- ALTERNATE ---- (BUT NOT EFFICIENT)
def main():
    sentance = input("Enter Number: ")
    word     = sentance.count(" ")
    print(f"Result = {word + 1}")
if __name__ == "__main__":
    main()
# ---- XXXXX -------

