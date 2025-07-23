import random
from hangman_word import word_list
from hangman_art import stages 
from hangman_art import logo 

#lives
lives = 5
print(logo)

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
    
    print(f"****************{lives}/6 LIVES LEFT****************")
    guess = input("Guess a lettter:  ").lower()

    #guessed already
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

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
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************It was {chosen_word}! YOU LOSE****************")

    if "_" not in display:
        game_over = True
        print("****************YOU WIN!****************")

    #lives / stages
    print (stages[lives])