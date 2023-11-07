#list of numbers 
# using input()
# writes "TRUE" if the first and last are the same
# otherwise write Fasle to the console

def main():
    wordList = input("Enter list of numbers: ").split(",")
    # splitting will put it in to a list on it's own
    if wordList[0] == wordList[-1]:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()