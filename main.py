#This is a script designed to test the expected value and best strategies of a handheld poker device
#Specifically, it is the 5 card draw poker machine, with the following rules
#
#With every hand, all cards are obtained from the player and shuffled back into the deck
#The player can bet 1-5 chips, with winnings based off of this betting amount
#The player can win the following amounts
#Royal flush      - 5000
#Straight flush   - 250
#Four of a kind   - 125
#Full House       - 40
#Flush            - 25
#Straight         - 20
#Three of a kind  - 15
#Two pair         - 10
#(p)Jack or better - 5
#
#Testing will be carried out using a list that keeps track of balance over time
#Will first create the ability to play the game
import deck as d
dick = d.Deck()





