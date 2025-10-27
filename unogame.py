import random

deck = []
colours = ["Red", "Blue", "Green", "Yellow"]
values = [0,1,2,3,4,5,6,7,8,9, "Draw Two", "Skip", "Reverse"]
wilds = ["Wild", "wild draw Four"]
#1.Generate the uno deck for the numbered and colored cards
def generate_deck():
    for colour in colours:
        for value in values:
            card = f"{value} {colour}"
            deck.append(card)
            if value != 0:
                deck.append(card)
    return deck
generate_deck()

#2.generate the wild cards
for i in range(4):
    deck.append(wilds[0])
    deck.append(wilds[1]) 
#3. Shuffle the cards
random.shuffle(deck)
Unodeck = deck
print(Unodeck)
#4. Function to deal cards to players
#def deal_cards(num_players, cards_per_player):
 

   




    
  

    