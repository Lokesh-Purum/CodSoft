import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    # Update scores label
    scores_label.config(text=f"You: {user_score}  Computer: {computer_score}")
    
    return result

# Function to handle user choice
def user_choice_clicked(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    
    result = determine_winner(choice, computer_choice)
    
    # Update result label with user and computer choices and result
    result_label.config(text=f"Your choice: {choice.capitalize()}\nComputer's choice: {computer_choice.capitalize()}\nResult: {result}")
    
    # Enable play again button
    play_again_button.config(state=tk.NORMAL)

# Function to reset scores and start a new game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    scores_label.config(text=f"You: {user_score}  Computer: {computer_score}")
    result_label.config(text="")
    play_again_button.config(state=tk.DISABLED)  # Disable play again button

# Main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg="#f0f0f0")  # Light gray background color

# Color scheme
bg_color = "#f0f0f0"  # Light gray background
button_color = "#4CAF50"  # Green button color
text_color = "#333333"  # Dark gray text color

# GUI Elements
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 18, "bold"), bg=bg_color, fg=text_color)
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose your move:", font=("Helvetica", 12), bg=bg_color, fg=text_color)
instruction_label.pack()

# Buttons for user choices
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: user_choice_clicked("rock"), bg=button_color, fg="white")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: user_choice_clicked("paper"), bg=button_color, fg="white")
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: user_choice_clicked("scissors"), bg=button_color, fg="white")
scissors_button.grid(row=0, column=2, padx=10)

# Scores label
scores_label = tk.Label(root, text=f"You: {user_score}  Computer: {computer_score}", font=("Helvetica", 14), bg=bg_color, fg=text_color)
scores_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg=bg_color, fg=text_color)
result_label.pack(pady=20)

# Reset game button (play again)
play_again_button = tk.Button(root, text="Play Again", state=tk.DISABLED, command=reset_game, bg=button_color, fg="white")
play_again_button.pack(pady=10)

# Run the main loop
root.mainloop()
