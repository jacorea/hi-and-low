#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import modules.
import random
from replit import clear
from art import logo

# Define constants.
DIFFICULTY_LEVELS = {
    "easy": 10,
    "hard": 5
}

# Draw a mystery number as the answer
answer = random.randint(0,101)

# end over
end_game = False

# Define a function to check if the guess is correct
def check_guess(guess, ans):
  global end_game
  if guess == ans:
      print(f"You got it! The answer was {ans}")
      end_game = True
      
  elif guess < ans:
      print("Too low.")
  else:
      print("Too high.")
  return False

def hi_or_low(num_lives):
  # help user with how many lives they have
  print(f"You have {num_lives} lives remaining.")
  # Ask the player to guess the number.
  user_guess = int(input("Make a guess: "))
  # Check if the guess is correct.
  check_guess(user_guess, answer)


def play_game(): 
  #global variable
  global end_game 
  # print logo
  print(logo)
  # Starting print statements
  print("Welcome to the Numbers guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  user_mode = input("Choose a difficulty level: Type 'easy' or 'hard':  ")

  # Set number of lives based on user difficuly level
  lives = DIFFICULTY_LEVELS[user_mode]
  
  # play game with condition 
  while not end_game:
    hi_or_low(lives)
    lives -= 1
    if lives == 0:
      print("You lost.")
      print(f"The answer was {answer}.")
      end_game = True 

play_game()

# restarting game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


      
