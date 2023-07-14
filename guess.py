import random
import time

words = ["julio", "rings", "mouse", "swim", "flame", "proud", "crisp", "solar", "grace", "swift", "blush", "fairy", "crown", "panda", "table", "fruit", "green", "brush", "photo", "music", "climb", "shirt", "sweet", "peace", "laugh", "world"]
letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ç","z","x","c","v","b","n","m"]
y = 0
x = 0
z = 0
w = 0
c = 0
v = 0
match = ["?","?","?","?","?"]
wrong = []
none = []
word = "a"
rand = random.choice(words)

print("\nYou have to guess a random word the game generated! \nYou only have 5 guesses, use them wisely!\nOnly words with 5 letters are accepted.")

while y < 5:
    if y == 0:
        word = input("\nwrite the "+str(y+1)+"st word: ")
    else:
        word = input("\nwrite the "+str(y+1)+"th word: ")

    while (len(word)) != 5:
        print("word length greater or less than 5")
        if y == 0:
            word = input("\nwrite the "+str(y+1)+"st word: ")
        else:
            word = input("\nwrite the "+str(y+1)+"th word: ")
    for x in range(0,len(words)):
        if word == rand:
            print("you won")
            quit()
    for z in range(0, 5):
        if word[z] == rand[z]:
            match[z] = word[z]
            if word[z] in wrong:
                wrong.remove(word[z])
        else:
            if word[z] in rand:
                if word[z] not in wrong:
                    wrong.append(word[z])
            if word[z] not in rand and word[z] not in none:
                none.append(word[z])
    for v in range(0,len(wrong)):
        if wrong[v] in letters:
            letters.remove(wrong[v])
    print("")
    for w in range(0,5):
        print(match[w], end="")
    if len(wrong) > 0:
        print("")
        print("\nletters in the word in wrong places: ")
        for w in range(0,len(wrong)):
            print(wrong[w], end=" ")
    if len(none) > 0:
        print("")
        print("\nletters that are not in the word: ")
        for w in range(0, len(none)):
            print(none[w], end=" ")
    print("")
    print("")
    print("available letters")
    for c in range(0,len(letters)):
        print(letters[c], end=" ")
    print("")
    y = y + 1
    print("")
print("You Lost :(\nThe word was "+rand)
time.sleep(10)
