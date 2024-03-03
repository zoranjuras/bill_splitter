sequence = input()

for char in sequence:
    if not char.isalpha():
        break
    else:
        if char in "aeiou":
            print("vowel")
        else:
            print("consonant")
