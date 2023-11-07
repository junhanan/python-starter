
# def main():
#     print(uppersOrLower())

# def uppersOrLower():
#     str1 = "HeLLO"
    
#     for letter in str1:
#         if letter != letter.upper():
#             return False
#     return True

# if __name__ == "__main__":
#     main()




# trye if uppercase
# interate through the string and check if it's character upper
# if it's not upper breakout and = false

def main():
    
    str1 = "HeLLO"
    
    bool = True
    for letter in str1:
        if letter != letter.upper():
            print(False)
            bool = False
            break
        break

    print(bool)

if __name__ == "__main__":
    main()
            