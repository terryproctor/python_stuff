userWord = input("please enter a word:\n ")
newWord = userWord.upper()

vowels =('A','E','I','O','U')
for x in vowels:
    newWord = newWord.replace(x,"*")

print(newWord)