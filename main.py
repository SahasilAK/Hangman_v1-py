import random
from hangman_words import word_list
from hangman_art import stages, logo



chosen_word = random.choice(word_list)
print(logo)
display = []

word_length = len(chosen_word)


for letter in range(word_length):
	display +="_"


print(display)	
life = 6

end_of_game = False

while not end_of_game:
	guess = input('Guess a letter: ').lower()
	

	for position in range(word_length):
		letter = chosen_word[position]

		if letter == guess:
			display[position] = letter 

	if guess not in chosen_word:
		if life == 0:
		 	end_of_game = True
		 	word = "".join(chosen_word)
		 	print(f"!!!!!Uh Oh Your guess was wrong the word was \'{word}\'!!!!!")
		 	break
		life -= 1
		
		



	print(display)

	if "_" not in display:
		end_of_game = True
		word = ''.join(display)
		print(f'!!!!Your Guess Was Correct, the word was \"{word.upper()}\"!!!!')

	else:
	    end_of_game = False	
	
	print(stages[life])