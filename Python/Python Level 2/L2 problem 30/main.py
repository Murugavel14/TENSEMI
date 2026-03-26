#Python Level 2 | Problem 30
def main():
   # Your Code Here
    a=int(input("Enter no.1 :"))
    b=int(input("Enter no.2 :"))
    small=min(a,b)
    while True:
        if(a%small==0 and b%small==0):
            hcf=small
            break
        small=small-1
    print("HCF :",hcf)
if __name__ == "__main__":
    main()