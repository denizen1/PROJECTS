import random
from hangman_word import word_list
from hangman_art import stages

#lives
lives = 5


#randomly choose a word
chosen_word = random.choice(word_list)
print(chosen_word)

#create a placeholder
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


#ask the user to guess the word and  while loop to repeatedly guess
game_over = False
correct_letters = []
while not game_over:

    guess = input("Guess a lettter:  ").lower()

    #if its right and wrong acc instead step 2 "display"
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    #lives reduces by 1 
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You win")

    #lives / stages
    print (stages[lives])