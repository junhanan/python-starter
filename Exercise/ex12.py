
def main():
    choice = int(input("Enter integer: "))
    if choice > 0:
        choice = 0 - choice
    elif choice == 0:
        choice = 0
    else:
        choice = 0 - choice
    
    print(choice)

if __name__ == "__main__":
    main()