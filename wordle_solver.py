from nltk.corpus import words

word_list = words.words()

word_length = int(input("How long is the word?: "))
wordle_list = [word for word in word_list if len(word) == word_length]

yellow_letters = set([char for char in input("yellow letters: ")])
possible_words = [word for word in wordle_list if yellow_letters.issubset(word)]

grey_letters = [char for char in input("grey letters: ")]
possible_words = [word for word in possible_words if 1 not in [c in word for c in grey_letters]]

for i in range(word_length):
    if input(f'letter #{i+1} green? (y/n): ').lower() == 'y':
        green = input(f'Enter {i+1}st letter: ')
        possible_words = [str(word) for word in possible_words if word.find(green) == i]


print(possible_words)