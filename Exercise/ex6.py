
def main():
    lst = [11, 100, 101, 999, 1001]
    
    new_lst = []
    for num in lst[::-1]:
        new_lst.append(num)

    print(new_lst)

if __name__ == "__main__":
    main()