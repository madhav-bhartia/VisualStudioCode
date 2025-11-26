import tkinter as tk
from tkinter import messagebox
import random

# Expanded list of possible words
words = [
    'python', 'hangman', 'challenge', 'programming', 'openai', 'advanced', 'development',
    'algorithm', 'binary', 'compiler', 'data', 'encryption', 'function', 'gigabyte', 'hardware',
    'internet', 'java', 'kernel', 'linux', 'machine', 'network', 'object', 'protocol', 'query',
    'robotics', 'software', 'technology', 'unicode', 'variable', 'web', 'xml', 'yield', 'zip',
    'array', 'buffer', 'cache', 'debug', 'exception', 'framework', 'graphics', 'hash', 'interface',
    'json', 'keyboard', 'library', 'module', 'node', 'operating', 'pointer', 'queue', 'recursion',
    'stack', 'thread', 'utility', 'virtual', 'wireless', 'xml', 'yottabyte', 'zen'
]

class HangmanGame:
    def __init__(self, root, max_attempts=6):
        self.root = root
        self.root.title("Hangman Game")

        self.word = random.choice(words).upper()
        self.guesses = set()
        self.max_attempts = max_attempts
        self.attempts = 0

        self.reveal_letters()
        self.create_widgets()
        self.update_display()

    def reveal_letters(self):
        num_revealed = random.randint(1, max(1, len(self.word) // 4))
        revealed_indices = random.sample(range(len(self.word)), num_revealed)
        for idx in revealed_indices:
            self.guesses.add(self.word[idx])

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack(pady=10)
        self.draw_hangman()

        self.word_label = tk.Label(self.root, font=('Comic Sans MS', 18))
        self.word_label.pack(pady=10)

        self.guesses_label = tk.Label(self.root, text="Guesses: ", font=('Comic Sans MS', 14))
        self.guesses_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=('Comic Sans MS', 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.make_guess)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.max_attempts}", font=('Comic Sans MS', 14))
        self.attempts_label.pack(pady=10)

    def update_display(self):
        display_word = ' '.join([letter if letter in self.guesses else '_' for letter in self.word])
        self.word_label.config(text=display_word)
        self.guesses_label.config(text=f"Guesses: {' '.join(sorted(self.guesses))}")
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

    def make_guess(self, event):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(guess) == 1 and guess.isalpha() and guess not in self.guesses:
            self.guesses.add(guess)
            if guess not in self.word:
                self.attempts += 1
                self.draw_hangman()
            self.update_display()
            self.check_game_status()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single valid letter that you haven't guessed before.")

    def check_game_status(self):
        if all(letter in self.guesses for letter in self.word):
            messagebox.showinfo("Hangman", "Congratulations! You've guessed the word correctly!")
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Hangman", f"Game Over! The word was {self.word}.")
            self.reset_game()

    def reset_game(self):
        self.word = random.choice(words).upper()
        self.guesses.clear()
        self.attempts = 0
        self.reveal_letters()
        self.update_display()
        self.draw_hangman(reset=True)

    def draw_hangman(self, reset=False):
        self.canvas.delete("all")

        # Draw the base
        self.canvas.create_line(10, 190, 190, 190, width=2)  # Ground line
        self.canvas.create_line(50, 190, 50, 20, width=2)    # Vertical pole
        self.canvas.create_line(50, 20, 150, 20, width=2)    # Horizontal pole
        self.canvas.create_line(150, 20, 150, 40, width=2)   # Short vertical line (gallows)

        if reset:
            return

        # Draw parts based on the number of wrong attempts
        match self.attempts:
            case 1:
                self.canvas.create_oval(130, 40, 170, 80, width=2)  # Head
            case 2:
                self.canvas.create_line(150, 80, 150, 140, width=2)  # Body
            case 3:
                self.canvas.create_line(150, 100, 120, 80, width=2)  # Left arm
            case 4:
                self.canvas.create_line(150, 100, 180, 80, width=2)  # Right arm
            case 5:
                self.canvas.create_line(150, 140, 130, 170, width=2)  # Left leg
            case 6:
                self.canvas.create_line(150, 140, 170, 170, width=2)  # Right leg

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
