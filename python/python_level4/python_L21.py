def main():
count = 0
for i in range (11,100):
    pc = True
    for j in range (2, i):
        if(i % j == 0):
            pc = False
            break
    if pc:
        count += 1
print(count)
if __name__ == "__main__":
    main()
