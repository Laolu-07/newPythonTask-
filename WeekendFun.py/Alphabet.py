letter = input("Enter one letter: ").lower()

if len(letter) == 1 and letter.isalpha():
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
