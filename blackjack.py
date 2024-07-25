import random
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
      
from art import logo
print(logo)

print("Welcome to the Game of BlackJack!\n")

def card_distribution():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def final(user_score, computer_score):
  if user_score == computer_score:
    return "\nDraw!"
  elif computer_score == 0:
    return "\nYou lost! Computer has a blackjack."
  elif user_score == 0:
    return "\nYou won with a blackjack!"
  elif user_score > 21:
    return "\nYou lose! Your Score is above 21."
  elif computer_score > 21:
    return "\nYou win! Computer's score is above 21."
  elif user_score > computer_score:
    return "\nYou win!"
  else:
    return "\nYou lose!"

def game():
  
  user_cards=[]
  computer_cards=[]
  game_over = False
  
  def calculation(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    else:
      return sum(cards)
  
  for _ in range(2):
    user_cards.append(card_distribution())
    computer_cards.append(card_distribution())
  
  while not game_over:
    user_score = calculation(user_cards)
    computer_score = calculation(computer_cards)
    
    print(f"\n Your cards are {user_cards} and score is: {user_score}.")
    print(f" Computer's first card is: {computer_cards[0]}.")   
    
    if user_score == 0 or computer_score == 0 or user_score>21:
      game_over = True
    else:
      again_deal = input("\nType 'y' for card or 'n' to pass.").lower()
      if again_deal == 'y':
        user_cards.append(card_distribution())
      else:
        game_over = True
  
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(card_distribution())
    computer_score = calculation(computer_cards)    
  
  print(f"\n Your final deck is {user_cards} and score is {user_score}.")
  print(f" Computer's final deck is {computer_cards} and score is {computer_score}")
  print(final(user_score, computer_score))

while input("Do you want to play? 'y' or 'n'.").lower() == 'y':
  clear_console()
  game()
  