import tkinter as tk
import core 

def refresh() -> None:
    """Update the UI based on the state of 'core'."""
    label.config(text=core.get_masked_word(), fg="white")
    chances_label.config(text=f"Chances Left: {core.lives}")
    wrong_label.config(text=core.get_wrong_text())

    if "_" not in core.guessed:
        label.config(text="YOU WIN!", fg="green")
        show_reveal()
        disable_keyboard()
    elif core.lives <= 0:
        label.config(text="GAME OVER!", fg="red")
        show_reveal()
        disable_keyboard()
    else:
        hide_reveal()
        enable_keyboard()
    
# === UI Actions ===
def on_guess(letter: str) -> None:
    core.guess(letter)
    refresh()

def on_easy() -> None:
    core.easy()
    refresh()

def on_medium() -> None:
    core.medium()
    refresh()

def on_hard() -> None:
    core.hard()
    refresh()

def on_restart() -> None:
    core.start_new_game()
    refresh()

def on_submit() -> None:
    """Takes the second player word, hide the widgets and the new word (deactivated by default)."""
    ok = core.submit_multiplayer(Player2_Entry.get())
    if ok:
        Player2_Entry.delete(0, tk.END)
        Multiplayer_label.grid_forget()
        Player2_Entry.grid_forget()
        sbn_button.grid_forget()
        refresh() 

# === UI utilities ===

def disable_keyboard() -> None:
    for btn in btn_frame.winfo_children():
        btn["state"] = tk.DISABLED

def enable_keyboard() -> None:
    for btn in btn_frame.winfo_children():
        btn["state"] = tk.NORMAL

def hide_reveal() -> None:
    word_label.grid_remove()

def show_reveal() -> None:
    word_label.config(text=core.get_reveal_text())
    word_label.grid(row=7, column=0, columnspan=10, pady=20)

# === Game ===
if __name__ == "__main__":
    game = tk.Tk()
    game.title("THE HANGMAN GAME")

    menubar = tk.Menu(game)
    game.config(menu=menubar)
    difficulty_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Difficulty", menu=difficulty_menu)
    difficulty_menu.add_command(label="Easy", command=on_easy)
    difficulty_menu.add_command(label="Medium", command=on_medium)
    difficulty_menu.add_command(label="Hard", command=on_hard)

    label = tk.Label(game, text=core.get_masked_word(), font=("Helvetica", 24))
    chances_label = tk.Label(game, text=f"Chances Left: {core.lives}", font=("Helvetica", 18))
    wrong_label = tk.Label(game, text=core.get_wrong_text(), font=("Helvetica", 18), fg="red")

    btn_frame = tk.Frame(game)
    rows = ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]
    for r, row in enumerate(rows):
        for c, letter in enumerate(row):
            tk.Button(
                btn_frame,
                text=letter.upper(),
                command=lambda l=letter: on_guess(l),
                height=2, width=4,
            ).grid(row=r, column=c, padx=5, pady=5)

    restart_button = tk.Button(game, text="RESTART GAME", font=("Helvetica", 16), command=on_restart)

    word_label = tk.Label(game, text=core.get_reveal_text(), font=("Helvetica", 20), fg="gray")
    word_label.grid(row=7, column=0, columnspan=10, pady=20)
    hide_reveal()

    Multiplayer_label = tk.Label(game, text="MULTIPLAYER", font=("Helvetica", 18))
    Player2_Entry = tk.Entry(game, font=("Helvetica", 16))
    sbn_button = tk.Button(game, text="Submit", font=("Helvetica", 16), command=on_submit)

    # Layout
    label.grid(row=0, column=0, columnspan=10, pady=20)
    chances_label.grid(row=1, column=0, columnspan=10, pady=10)
    wrong_label.grid(row=2, column=0, columnspan=10, pady=10)
    btn_frame.grid(row=3, column=0, columnspan=10, pady=20)
    restart_button.grid(row=6, column=0, columnspan=10, pady=20)
    Multiplayer_label.grid(row=8, column=0, columnspan=10, pady=10)
    Player2_Entry.grid(row=9, column=0, columnspan=10, pady=10)
    sbn_button.grid(row=10, column=0, columnspan=10, pady=10)

    refresh()

    game.mainloop()

