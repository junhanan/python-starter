#input
# initialize
# prompt
# return the volume

def main():
    width = int(input("enter width: "))
    height = int(input("enter height: "))
    length = int(input ("enter length: "))

    volume = width * height * length

    print(f'Volume is: {volume}')

if __name__ == '__main__':
    main()

