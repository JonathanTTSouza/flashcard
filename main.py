from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_data)
    random_french_word = current_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(word, text=random_french_word, fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    random_english_word = current_card['English']
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word, text=random_english_word, fill='white')


word_data = pd.read_csv('data/french_words.csv').to_dict(orient="records")

# WINDOW
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

flip_timer = window.after(3000, func=flip_card)

# CANVAS IMAGES AND TEXT
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=next_word)
correct_button.grid(column=1, row=1)

next_word()

window.mainloop()
