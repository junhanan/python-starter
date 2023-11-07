
# program make list
'''
10 ran num
in list
0-100
use f-string to display
'''
import random

def main():
    
    lst = []
    for i in range(10):
        rand_num = random.randint(0, 100)
        lst.append(rand_num)
    
    sum1 = sum(lst)
    print(f"The sum is: {sum1}")

if __name__ == "__main__":
    main()