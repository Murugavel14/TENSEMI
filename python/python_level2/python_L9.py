def main():
    sum = 0
    for i in range(10,100,5):
        if (i % 10 == 5):
            sum = sum + i
    print(f"Result = {sum}")
if __name__ == "__main__":
    main() 
