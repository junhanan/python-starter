
def main():
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_count = 0
    con_count = 0
    strng = "Apple"

    for letter in strng:
        if letter in vowel_list:
            vowel_count += 1
        else:
            con_count += 1
    
    print(f"Vowels: {vowel_count}\nConsonants: {con_count}")

if __name__ == "__main__":
    main()