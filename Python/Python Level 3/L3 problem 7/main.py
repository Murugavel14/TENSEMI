#Python Level 3 | Problem 7
def function(n1,n2):
# Define and initialize no2
    no2 = 0
    if(n1==n2):
        return 1 
    else: 
        return 0
    # Your Program Here
def main():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    n3 = function(n1,n2)
    print(n3)
if __name__ == "__main__":
    main()