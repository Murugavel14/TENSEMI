def main():
    arr = [1, 4, 5, 8, 7, 6, 3]
    def array_to_number(arr):
        return int("".join(str(x) for x in arr))
    print(array_to_number(arr))
if __name__ == "__main__":
    main()
