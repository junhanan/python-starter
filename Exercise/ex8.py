

def main():
    myList = [6, 2, 7, 3, 77, 7, 1]
    min = myList[0]
    for num in myList:
        if num < min:
            min = num

    print(min)

if __name__ == "__main__":
    main()