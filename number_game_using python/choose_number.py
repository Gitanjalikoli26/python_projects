import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime

# --- Database Setup ---
def create_table():
    conn = sqlite3.connect("guess_game.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            guess INTEGER,
            result TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_attempt(username, guess, result):
    conn = sqlite3.connect("guess_game.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attempts (username, guess, result, timestamp) VALUES (?, ?, ?, ?)", 
                   (username, guess, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# --- Game Setup ---
SECRET_NUMBER = 5
MAX_ATTEMPTS = 3
attempts = 0
username = ""

# --- Game Logic ---
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess == SECRET_NUMBER:
        log_attempt(username, guess, "Success")
        messagebox.showinfo("Congratulations!", f"🎉 {username}, you guessed the number!")
        window.destroy()
    elif attempts >= MAX_ATTEMPTS:
        log_attempt(username, guess, "Failed")
        messagebox.showerror("Game Over", f"😢 Sorry {username}, out of attempts! The number was {SECRET_NUMBER}")
        window.destroy()
    else:
        log_attempt(username, guess, "Wrong")
        messagebox.showinfo("Try Again", f"❌ Wrong guess! Attempts left: {MAX_ATTEMPTS - attempts}")

# --- Ask for User Name ---
def get_username():
    global username
    username = simpledialog.askstring("Player Name", "Enter your name:")
    if not username:
        username = "Anonymous"

# --- GUI Setup ---
create_table()
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("350x250")
window.configure(bg="#f0f8ff")

get_username()  # Ask for the player's name before starting

tk.Label(window, text=f"Hello, {username}!", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#00688B").pack(pady=5)
tk.Label(window, text="Guess a number between 1 and 10:",
         font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#333366").pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), bg="#ffffff", fg="#333366")
entry.pack(pady=10)

tk.Button(window, text="Submit Guess", font=("Arial", 11),
          bg="#4682b4", fg="white", activebackground="#5a9bd4",
          activeforeground="white", command=check_guess).pack(pady=15)

window.mainloop()
