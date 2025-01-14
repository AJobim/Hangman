import random
import hangman_words
import hangman_art

lives = 6

chosen_word = (random.choice(hangman_words.word_list))
print(hangman_art.stages[lives])
print(chosen_word)
word_length = len(chosen_word)

displayList = []
display = ""

for position in range(word_length):
    displayList.append("_")

print("".join(displayList))

wrong_letters = []

while True:
    print(f"****************************<[{lives}]>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in display or guess in wrong_letters:
        print(f"You've already guessed the letter {guess.upper()}! Try another one!")
    elif guess not in chosen_word:
        lives -= 1
        wrong_letters.append(guess)
        print(f'The letter "{guess.upper()}" is not in the word, you lose a life!\n'
              f'The wrong letters are: {", ".join(wrong_letters)}')


    for index, letter in enumerate(chosen_word):
        if letter == guess:
            displayList[index] = guess
    display = "".join(displayList)

    print(display)

    if display == chosen_word or guess == chosen_word:
        print(f"***********************YOU WON**********************\n")
        break

    if lives == 0:
        print(f"***********************YOU LOSE**********************\n"
              f"The chosen word was: {chosen_word}")
        print(hangman_art.stages[lives])
        break

    print(hangman_art.stages[lives])
