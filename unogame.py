import random

deck = []
colours = ["Red", "Blue", "Green", "Yellow"]
values = [0,1,2,3,4,5,6,7,8,9, "Draw Two", "Skip", "Reverse"]
wilds = ["Wild", "Wild Draw Four"]
def generate_deck():
    """
    1. Generate the uno deck for the numbered and colored cards
    RETURNS deck: list of cards in the uno deck
    """

    for colour in colours:
        for value in values:
            card = f"{value} {colour}"
            deck.append(card)
            if value != 0:
                deck.append(card)
    return deck
deck = generate_deck()

#2.generate the wild cards
for i in range(4):
    deck.append(wilds[0])
    deck.append(wilds[1]) 
#3. Shuffle the cards
random.shuffle(deck)
UnoDeck = deck
def draw_card(deck):
    # Check if there are any cards left in the deck
    if len(deck) == 0:
        return "Deck is empty!"
    
    # 1. Take the very last card off the deck
    card_drawn = deck.pop()
# 2. Give the card back to whoever asked for it
    return card_drawn
   
new_card = draw_card(UnoDeck)
print(f"You drew a: {new_card}")
print(f"Cards left in deck: {len(UnoDeck)}")

 
Computer_Hand = []
Human_Hand = []

def dealing_cards():
    #Card dealing step
    global Computer_Hand, Human_Hand
    for _ in range(7):
        Computer_Hand.append(draw_card(UnoDeck))
        Human_Hand.append(draw_card(UnoDeck))

dealing_cards()
print("\n--- Starting Hands ---")
# ---  ---
print(f"Your Hand ({len(Human_Hand)} cards): {Human_Hand}")
print(f"Computer Hand ({len(Computer_Hand)} cards): {Computer_Hand}")
 
# --- Discard Pile Setup ---

discard_pile = []

# Draw a starting card that cannot be a wild card
while True:
    starting_card = draw_card(UnoDeck)
    # Check if the card is NOT a Wild or Wild Draw Four
    if starting_card not in ["Wild", "Wild Draw Four"]:
        discard_pile.append(starting_card)
        break
    else:
        # If it's a Wild, put it back in the deck and reshuffle to try again
        UnoDeck.append(starting_card)
        random.shuffle(UnoDeck)

print("\n--- Game Starts ---")
print(f"Current Card on Table: {discard_pile[-1]}")

def is_valid_play(card_to_play, top_card):
    """
    Checks if 'card_to_play' can be played on 'top_card'.
    
    Args:
        card_to_play (str): The card the player wants to put down.
        top_card (str): The card currently at the top of the discard pile.
        
    Returns:
        bool: True if the move is legal, False otherwise.
    """
    
    # 1. Handle Wild Cards: They can be played on anything
    if card_to_play in ["Wild", "Wild Draw Four"]:
        return True

    # 2. Get the color and value of both cards
    # Example: "5 Red" splits into ['5', 'Red']
    # Note: Wilds and Wild Draw Four don't have a space, so they are excluded above.
    
    # Split card to play (e.g., '5 Red' -> ['5', 'Red'])
    play_parts = card_to_play.split() 
    play_value = play_parts[0]
    play_colour = play_parts[-1] # The last part is the color (for action cards like 'Draw Two Blue')
    
    # Split top card
    top_parts = top_card.split()
    top_value = top_parts[0]
    top_colour = top_parts[-1]

    # 3. Check for matching colour OR matching value/action
    if play_colour == top_colour:
        # Card matches the colour
        return True
    elif play_value == top_value:
        # Card matches the number or action (e.g., '5' on '5', or 'Skip' on 'Skip')
        return True
    
    # If none of the conditions met, the play is invalid
    return False

# Example Test (you can remove this later)
# test_card_1 = "5 Red"
# test_card_2 = "Draw Two Blue"
# print(f"\nCan play '5 Red' on 'Draw Two Blue'? {is_valid_play(test_card_1, test_card_2)}")
# print(f"Can play 'Draw Two Blue' on '5 Red'? {is_valid_play(test_card_2, test_card_1)}")
# print(f"Can play '7 Red' on '5 Red'? {is_valid_play('7 Red', '5 Red')}")
# --- Game State Variables ---
# Use 0 for Human, 1 for Computer, or simply use a boolean/string
current_player = 0  # 0 means Human starts
game_running = True # Control the main loop
def main_game_loop():
    global current_player, game_running, Human_Hand, Computer_Hand, UnoDeck, discard_pile
    
    # Simple turn manager (0 = Human, 1 = Computer)
    current_player = 0 
    game_running = True

    while game_running:
        top_card = discard_pile[-1]
        
        # --- Human Player's Turn ---
        if current_player == 0:
            print("\n--------------------------------")
            print(f"Your Turn! Current Card: {top_card}")
            print(f"Your Hand ({len(Human_Hand)} cards): {Human_Hand}")
            
            # **Your next task: Implement human_turn()**
            human_turn(Human_Hand, top_card)

            # Check for win
            if not Human_Hand:
                print("🥳 Congratulations! You won UNO!")
                game_running = False
            
            # Switch to computer's turn
            current_player = 1

        # --- Computer Player's Turn ---
        else:
            print("\n--------------------------------")
            print(f"Computer's Turn... ({len(Computer_Hand)} cards)")
            
            # **Your next task: Implement computer_move()**
            computer_move(Computer_Hand, top_card)

            # Check for win
            if not Computer_Hand:
                print("💻 The Computer won UNO! Better luck next time.")
                game_running = False
                
            # Switch to human's turn
            current_player = 0
            
# Don't call this yet—you need to write the two turn functions first!
# main_game_loop()
def computer_move(hand, top_card):
    # Search for a playable card
    for card in hand:
        if is_valid_play(card, top_card):
            print(f"Computer plays: {card}")
            hand.remove(card)       # Remove card from computer's hand
            discard_pile.append(card) # Add card to discard pile
            # NOTE: Logic for action cards (Draw Two, Skip) and Wilds must be added later!
            return # End turn after playing one card
            
    # If no card is found, the computer must draw
    print("Computer draws a card.")
    new_card = draw_card(UnoDeck)
    hand.append(new_card)
    
    # A common UNO rule: if you draw and can play, you play it immediately.
    # For simplicity, we'll skip immediate play for now, but you can add it later.
    return
def human_turn(hand, top_card):
    while True:
        # Display the current state and hand options
        print(f"Top Card is: {top_card}")
        for i, card in enumerate(hand):
            print(f"[{i}]: {card}")
        print("[D]: Draw a Card")
        
        choice = input("Enter the number of the card to play, or 'D' to draw: ").upper()
        
        # 1. Handle Drawing a Card
        if choice == 'D':
            new_card = draw_card(UnoDeck)
            hand.append(new_card)
            print(f"You drew: {new_card}. Your turn ends.")
            break # End turn

        # 2. Handle Playing a Card
        try:
            card_index = int(choice)
            if 0 <= card_index < len(hand):
                card_to_play = hand[card_index]
                
                if is_valid_play(card_to_play, top_card):
                    # Play is valid:
                    hand.pop(card_index)      # Remove card from human's hand
                    discard_pile.append(card_to_play) # Add card to discard pile
                    print(f"You played: {card_to_play}")
                    # NOTE: Logic for action cards (Draw Two, Skip) and Wilds must be added later!
                    break # End turn
                else:
                    print("🚫 That's not a valid move. Try again.")
            else:
                print("Invalid number. Please choose a number from your hand.")
        except ValueError:
            print("Invalid input. Please enter a card number or 'D'.")




    
  

    