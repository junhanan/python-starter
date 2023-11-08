from datetime import datetime

def main():
    while True:
        input1 = input(f'Enter first integer: ')
        if input1 == "exit":
            break
        
        input2 = input(f'Enter second integer: ')
        if input2 == "exit":
            break
        
        operationInput = input(f'Enter operation (add, sub, mul, div): ')
        ans = 'z'
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
        log_file(input1, operationInput, input2, ans)

def log_file(input1, operation_input, input2, ans):
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y %I:%M:%S %p")

    with open("output.txt", "a") as f:
        f.write(f"{date_str}: {input1} {operation_input} {input2} = {ans}\n")

    pass

if __name__ == "__main__":
    main()
