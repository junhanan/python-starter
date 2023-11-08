def main():
    while True:
        input1 = input(f'Enter first integer: ')
        if input1 == "exit":
            break
        
        input2 = input(f'Enter second integer: ')
        if input2 == "exit":
            break
        
        operationInput = input(f'Enter operation (add, sub, mul, div): ')
        if operationInput == "add":
            ans = int(input1) + int(input2)
            print(f'Answer: {ans}')
        elif operationInput == "sub":
            ans = int(input1) - int(input2)
            print(f'Answer: {ans}')
        elif operationInput == "mul":
            ans = int(input1) * int(input2)
            print(f'Answer: {ans}')
        elif operationInput == "div":
            try:
                ans = int(input1) / int(input2)
                print(f'Answer: {ans}')
            except:
                print("are you an idiot???? you can't divide by 0")


if __name__ == "__main__":
    main()
