def main():
    y = 0
    for i in range(2,10):
        if i in (2, 3, 5, 7):
            y += i
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
