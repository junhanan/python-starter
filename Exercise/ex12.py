
def main():
    choice = input("Enter integer: ")

    try:
        choice = int(choice)
    except:
        print(f"{choice} is not an integer.")
        return

    choice = int(choice)
    if (choice) > 0:
        choice = 0 - choice
    elif choice == 0:
        choice = 0
    else:
        choice = 0 - choice

    print(choice)

if __name__ == "__main__":
    main()