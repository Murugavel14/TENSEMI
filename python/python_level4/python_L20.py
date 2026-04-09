def main():
    count = 0
    for i in range(1,10):
        if i in (2, 3, 5, 7):
            count += 1
    print(f"Result = {count}")
if __name__ == "__main__":
    main()
