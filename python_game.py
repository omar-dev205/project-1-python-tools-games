import random

def check_win(comp, user):
    if comp == user:
        return 0  # Draw
    elif (comp == 'r' and user == 's') or (comp == 'p' and user == 'r') or (comp == 's' and user == 'p'):
        return -1 # Computer wins
    else:
        return 1  # User wins

print("--- Welcome to Rock, Paper, Scissors ---")
user_score = 0
comp_score = 0

while True:
    comp_choice = random.choice(['r', 'p', 's'])
    user_input = input("\nEnter Rock(r), Paper(p), Scissors(s) or 'q' to Quit: ").lower()

    if user_input == 'q':
        break
    
    if user_input not in ['r', 'p', 's']:
        print("Invalid input! Please try again.")
        continue

    result = check_win(comp_choice, user_input)
    print(f"Computer chose: {comp_choice}")

    if result == 0:
        print("It's a Tie!")
    elif result == 1:
        print("You Win this round!")
        user_score += 1
    else:
        print("Computer Wins this round!")
        comp_score += 1

    print(f"Current Score -> You: {user_score} | Computer: {comp_score}")

print("\n--- Final Game Over ---")
print(f"Final Score -> You: {user_score} | Computer: {comp_score}")
