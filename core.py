from __future__ import annotations
import random
from typing import List

# === Global State ===
words: List[str] = [
    "bear", "apple", "alice",
    "cherry", "forever", "lights",
    "punk", "random", "turtle",
]

word: str = random.choice(words)
guessed: List[str] = ["_" for _ in word]
incorrect_guesses: List[str] = []
lives: int = 7
multiplayer_mode: bool = False
game_over: bool = False
difficulty: str = "" 

# === Helpers ===
def get_masked_word() -> str:
    return " ".join(guessed)

def get_wrong_text() -> str:
    return "Incorrect Guesses: " + " ".join(incorrect_guesses)

def get_reveal_text() -> str:
    return "The Word Was: " + word

# === Difficulty === 
def easy() -> None:
    """Select Easy difficulty and start a new game. 
    
    Effects: 
        - Sets 'difficulty to "Easy".
        - Sets 'lives' to 10.
        - Starts a new game. 
    """
    global lives, difficulty
    difficulty = "Easy"
    lives = 10
    start_new_game(10)

def medium() -> None:
    """Select Medium difficulty and start a new game. 
    
    Effects: 
        - Sets 'difficulty to "Medium".
        - Sets 'lives' to 7.
        - Starts a new game. 
    """
    global lives, difficulty
    difficulty = "Medium"
    lives = 7
    start_new_game(7)

def hard() -> None:
    """Select Hard difficulty and start a new game.

    Effects:
        - Sets `difficulty` to "Hard".
        - Sets `lives` to 5.
        - Starts a new game.
    """
    global lives, difficulty
    difficulty = "Hard"
    lives = 5
    start_new_game(5)
    
# === Game === 
def start_new_game(chances: int | None = None) -> None:
    """Reset the game according to mode and difficulty (Single player by default)."""
    
    global word, guessed, lives, game_over, incorrect_guesses, multiplayer_mode, difficulty
    
    game_over = False
    
    word = random.choice(words)
    guessed = ["_" for _ in word]
    
    if difficulty == "":
        difficulty = "Medium"
    
    if chances is not None:
        lives = chances
    else: 
        lives = 10 if difficulty == "Easy" else 5 if difficulty == "Hard" else 7
        
    incorrect_guesses.clear()
    
    multiplayer_mode = False
    
def submit_multiplayer(candidate: str) -> bool:
    """Set multiplayer word from input; returns True on success."""
    global word, guessed, multiplayer_mode, game_over

    candidate = candidate.strip().lower()
    if not candidate:
        return False

    word = candidate
    guessed = ["_" for _ in word]
    game_over = False
    multiplayer_mode = True
    return True

def guess(letter: str) -> None:
    """Process a player's guessed letter and update lives / guessed / incorrect list.
    
    Args:
        letter(str): Letter selected by the player.
    """
    global lives, game_over

    if game_over:
        return
    
    letter = letter.lower()

    if letter in word:
        update_guessed(letter)  
    else:
        if letter not in incorrect_guesses:
            incorrect_guesses.append(letter)
        lives -= 1
        
    if "_" not in guessed or lives <= 0:
        game_over = True
        
def update_guessed(letter: str) -> None:
    """Reveal the correct letter in the masked word.
    
    Args:
        letter(str): Letter selected by the player.
        
    Effects:
        - Updates the 'guessed' list. 
    """
    for index, char in enumerate(word): 
        if char == letter:
            guessed[index] = letter


        
