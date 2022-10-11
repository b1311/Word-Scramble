base_word = input("Enter a word to show all scrambles: ")
scrambles = []
word = {}

def scramble(wor, scramble_word, c):

    for letter in wor:
        scramble_word = str(scramble_word) + str(letter)
        word[c] = wor.replace(letter, "", 1)
        #print("Scramble" + str(c) + ": " + scramble_word)
        #print("Letters remaining: " + word[c])

        if len(word[c]) >= 2:

            scramble(word[c], scramble_word, c+1)
        elif len(word[c]) == 1:
            print(scramble_word + word[c])
            scrambles.append(str(scramble_word) + str(word[c]))
        else:
            print("error")

        scramble_word = scramble_word.replace(letter, "", 1)

scramble(base_word, "", 1)