def main():
    #2 inputs until exit is typed

    while True:
        input1 = input(f'Enter first integer: ')
        if input1 == "exit":
            break
        
        input2 = input(f'Enter second integer: ')
        if input2 == "exit":
            break

        ans = int(input1) + int(input2)
        print(f'Answer: {ans}')

if __name__ == "__main__":
    main()

