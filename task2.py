import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result_label.config(text="Too low!")
        elif guess > number:
            result_label.config(text="Too high!")
        else:
            result_label.config(text="Correct! You guessed it!")
    except ValueError:
        result_label.config(text="Enter a valid number.")
    entry.delete(0, tk.END)

number = random.randint(1, 100)

root = tk.Tk()
root.title("Guess the Number")

tk.Label(root, text="Guess a number between 1 and 100").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit", command=check_guess).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
