﻿wordWithoutVowels = ""

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVowels += letter
		
print(wordWithoutVowels)