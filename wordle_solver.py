import tkinter

from english_words import english_words_set


word_list = english_words_set

word_length = int(input("How long is the word?: "))
possible_words = [word for word in word_list if len(word) == word_length]

yellow_letters = [char for char in input("yellow letters: ")]
if yellow_letters:
    possible_words = [word for word in possible_words if 1 in [c in word for c in yellow_letters]]

grey_letters = [char for char in input("grey letters: ")]
possible_words = [word for word in possible_words if 1 not in [c in word for c in grey_letters]]

for i in range(word_length):
    green = input(f'Enter letter #{i+1} (if unknown, hit Enter): ')
    if green != '':
        if green[0] == '!':
            possible_words = [str(word) for word in possible_words if word[i] != green[1]]
        else:
            possible_words = [str(word) for word in possible_words if word[i] == green]

app = tkinter.Tk()
app.title("Wordle Solver")
scroll = tkinter.Scrollbar(app)
listbox = tkinter.Listbox(app, height=35, width=40, yscrollcommand=scroll.set)
for i in range(len(possible_words)):
    listbox.insert(i, possible_words[i])
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox.pack()
app.mainloop()
