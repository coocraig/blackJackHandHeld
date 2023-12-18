# This module specifies classes and functions for a single player version of the blackjack game
# The premise is that the player has a set of chips granted to them every game
# And can play the game by betting 5 chips, being dealt a hand, then choosing which cards to give back to the dealer,
# and recieving whatever amount of chips coincides to their final hand
import deck as d

def new_game(tokens):
    print('''                                                            
                                88                          
                                ""                          
                                                            
 ,adPPYba, ,adPPYYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYba,   
a8"     "" ""     `Y8 I8[    "" 88 88P'   `"8a a8"     "8a  
8b         ,adPPPPP88  `"Y8ba,  88 88       88 8b       d8  
"8a,   ,aa 88,    ,88 aa    ]8I 88 88       88 "8a,   ,a8"  
 `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"' 88 88       88  `"YbbdP"'   
                                                            
                                                            ''')
    print("Welcome to the cracked casino. We only play 5-card blackjack here.")

    mydeck = d.Deck()
    # mydeck.shuffle()
    while(tokens >= 5):
        tokens = tokens - 5
        print(f"You now have {tokens} chips")
        hand = mydeck.deal(5)
        print(f"Your hand is as follows: ")
        for i in range(len(hand)):
            print(f"{i+1}.) {hand[i]}")

        response = input("\nEnter which cards you'd like to exchange, in any order [(e.g) 512, 251, 413, 35, 1]: ")

        # Sorting the response string to be descending to allow for the pop function to work the best
        to_Remove = sorted([int(char) - 1 for char in response], reverse=True)

        # Removing the cards from their hand
        for i in to_Remove:
            hand.pop(i)

        # Adding new cards to their hand
        hand.extend(mydeck.deal(len(to_Remove)))

        print(f"Your new hand is as follows: ")
        for i in range(len(hand)):
            print(f"{i + 1}.) {hand[i]}")

        break

def contains_Specific_Card(r, s, group):
    return any(c.rank == r and c.suit == s for c in group)

