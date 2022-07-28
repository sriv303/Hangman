import random
f = open("words.txt", "r")
words = [x for x in f]
f.close()
r = random.randint(0, len(words))
word = words[r].strip()
l_word = [x for x in word]
lives = 9
print('_'*(len(word)))
guess = ("_"*len(word))
while lives > 0 and guess!=word:
    inp = input("\nEnter character: ")
    while len(inp) != 1:
        inp = input("\nEnter character: ")
    if inp in word:
        indices = [i for i, x in enumerate(l_word) if x == inp]
        for i in indices:
            guess = guess[:i] + inp + guess[i+1:]
        print(guess)
        if guess == word:
            print("You Won!")
    else:
        lives-=1
        print(guess)
        if lives == 0:
            print("You Lose!")
    
