# adds list to the set

def main():
    lst = [1, 2, 3]
    mySet = {3, 4, 5}

    for num in lst:
        mySet.add(num)
    
    print(mySet)

if __name__ == "__main__":
    main()