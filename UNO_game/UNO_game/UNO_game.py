import random
colors = ['red', 'blue', 'green', 'yellow']
num_act = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
wild_cards = ['draw_4', 'wild']
action_cards = ['reverse', 'skip', 'draw_2', 'zero']
extra = 'card'
game_con = True
reverse = False
change = False

class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return (self.number + ' ' + self.color)

class Deck:

    #Creates the deck and each card
    def __init__(self):
        self.deck = []
        for color in colors:
            for number in num_act:
                self.deck.append(Card(color,number))
                self.deck.append(Card(color,number))

        for wild in wild_cards:
            self.deck.append(Card(extra, wild))
            self.deck.append(Card(extra, wild))
            self.deck.append(Card(extra, wild))
            self.deck.append(Card(extra, wild))

        for color in colors:
            for action in action_cards:
                self.deck.append(Card(color,action))

    #This could be used to print out the deck
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'This deck has: ' + deck_comp
    
    #This will randomly shuffle the deck created
    def shuffle(self):
        random.shuffle(self.deck)

    #This will be used to select a card from the deck
    def deal(self):
        single_card = self.deck.pop()
        return str(single_card)

class Hand:

    #This will create a hand of cards
    def __init__(self):
        self.cards = []

    #This will add one card to any hand
    def add_card(self, card):
        self.cards.append(card)

    #Used to print out objects
    def __str__(self):
        for i in self.cards:
            word = str(i)
        return word

    #Will check to see if a card can be removed
    def remove_card(self, card, card_played):
        
        card_split = card.split(' ')
            
        if card_split[0] in card_played:
            return True

        elif card_split[1] in card_played:
            return True

        elif (card_split[0] == 'draw_4'):
            return True

        elif (card_split[0] == 'wild'):
            return True

        else:
            return False


class Check():

    def __init__(self, card):
        self.card = card

    #Will be called to add four cards
    def draw4(self, player):
        count = 0
        if self.card.split()[0] == 'draw_4':
            while count < 4:
                player.add_card(deck.deal())
                count += 1
            return True

    #Will be called to add two cards
    def draw2(self, player):
        count = 0
        if self.card.split()[0] == 'draw_2':
            while count < 2:
                player.add_card(deck.deal())
                count += 1

    #Will be called to check for a skip card
    def skip(self):
        if self.card.split()[0] == 'skip':
            return True

    #Will be called to check for a reverse card
    def reverse(self):
        if self.card.split()[0] == 'reverse':
            return True

#Used to display the cards in the list
def show_cards(player):
    for i in player.cards:
        print(i)

#This if going to be called at start of the game to give each player 7 cards
def adding_cards(player):
    count = 0
    while count < 7:
        player.add_card(deck.deal())
        count += 1

#This is going to be called to check for a winner
def win(player):
    if len(player) == 0:
        return True

print("Welcome to UNO!\n")
print("Chances are you have already played this game before but just in case you don't know the rules, here they are: \n")
print("\tThis is going to be a two player game where each player will be given 7 cards total.")
print("\tOne of the players will be randomly selected to start the game.")
print("\tEach player will be shown their deck and in order to play a card you must type thr name of the card you would like to play.")
print("\tEach player is able to match either the color or the number to the current card that is out to play on.")
print("\tEach player will also be able to play action cards, which are: skips, reverse, draw_2, draw_4 and wild card.")
print("\tIf a player doesnt have a card to play just type draw to draw a new card from the deck.\n")

while True:
    try:
        ready = str(input("Okay now that you know how to play are you ready to play? Enter 'Yes' or 'No'. \n"))
        if ready.lower() == 'yes':
            game_con = True
            break

        elif ready.lower() == 'no':
            game_con = False
            break
    except TypeError:
        print("Please Enter 'Yes' or 'No'.\n")
        continue

while game_con == True:
    #Create the Deck
    deck = Deck()
    deck.shuffle()

    #Random start card
    card_played = 'two red'

    
    player1 = False
    player2 = False
    game_playing = True

    #Randomly generate first to play
    number = random.randint(1,2)
    if number == 1:
        player1 = True
    else:
        player2 = True


    #Create Each player's hand
    player_hand = Hand()
    player2_hand = Hand()

    #Adding cards to players hand
    adding_cards(player_hand)
    adding_cards(player2_hand)

    
    while game_playing == True:
        
        #Code for player 1
        while player1 == True:
            
            #Check if reverse is still active
            if reverse == True:

                #Check for a draw4 or a draw2 card
                check = Check(card_played)
                check.draw4(player_hand)
                check.draw2(player_hand)

                while True:
                    print('\n'*100)
                    if change == True:
                        card_played = new_color
                        print('Card in play: ' + card_played + '\n')
                        change = False
                    else:
                        print('Card in play: ' + card_played + '\n')

                    print('player 1 cards: \n')
                    show_cards(player_hand)
                    try:
                        next_card = str(input('\nWhich card would you like to play? Or type Draw.\n'))

                    except TypeError:
                        print("\nPlease input a card or draw\n")

                    if next_card.lower() == 'draw':
                        player_hand.add_card(deck.deal())

                    elif next_card.split()[0] == 'draw_4' or next_card.split()[0] == 'wild':
                        ans = str(input('What color would you like to play?\n'))
                        new_color = 'card ' + ans
                        change = True
                        break

                    elif next_card == '\n':
                        print("\nPlease input a card or draw\n")

                    elif next_card not in player_hand.cards:
                        print("\nThis card is not in your hand")

                    else:
                        break  

                check2 = Check(next_card)

                #Check for Skip
                if check2.skip() == True:
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player1 = True
                    player2 = False
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                #Check for Reverse
                elif check2.reverse() == True:
                    
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player1 = True
                    player2 = False
                    reverse = False
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                else:
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player1 = False
                    player2 = True
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break
            #If reverse not active continue with regular rotation
            else:

                #Check for a draw4 or a draw2 card
                check = Check(card_played)
                check.draw4(player_hand)
                check.draw2(player_hand)

                while True:
                    print('\n'*100)
                    if change == True:
                        card_played = new_color
                        print('Card in play: ' + card_played + '\n')
                        change = False
                    else:
                        print('Card in play: ' + card_played + '\n')

                    print('player 1 cards: \n')
                    show_cards(player_hand)
                    try:
                        next_card = str(input('\nWhich card would you like to play? Or type Draw.\n'))

                    except TypeError:
                        print("\nPlease input a card or draw\n")

                    if next_card.lower() == 'draw':
                            player_hand.add_card(deck.deal())

                    elif next_card.split()[0] == 'draw_4' or next_card.split()[0] == 'wild':
                        ans = str(input('What color would you like to play?\n'))
                        new_color = 'card ' + ans
                        change = True
                        break

                    elif next_card == '\n':
                        print("\nPlease input a card or draw\n")

                    elif next_card not in player_hand.cards:
                        print("\nThis card is not in your hand\n")

                    else:
                        break  

                check2 = Check(next_card)

                #Check for Skip
                if check2.skip() == True:
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue
                    player1 = True
                    player2 = False
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                #Check for Reverse
                elif check2.reverse() == True:
            
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player1 = True
                    player2 = False
                    reverse = True
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                else:
                    remove_check = player_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player_hand.cards.index(next_card)
                        player_hand.cards.remove(player_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player1 = False
                    player2 = True
                    if win(player_hand.cards) == True:
                        print('Player 1 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break



        #player 2 code
        while player2 == True:
            #Check if reverse is active
            if reverse == True:

                #Check for a draw4 or draw2 card
                check = Check(card_played)
                check.draw4(player2_hand)
                check.draw2(player2_hand)

                while True:
                    print('\n'*100)
                    if change == True:
                        card_played = new_color
                        print('Card in play: ' + card_played + '\n')
                        change = False
                    else:
                        print('Card in play: ' + card_played + '\n')
                    print('player 2 cards: \n')
                    show_cards(player2_hand)
                    try:
                        next_card = str(input('\nWhich card would you like to play? Or type Draw.\n'))

                    except TypeError:
                        print("\nPlease input a card or draw\n")

                    if next_card.lower() == 'draw':
                            player2_hand.add_card(deck.deal())

                    elif next_card.split()[0] == 'draw_4' or next_card.split()[0] == 'wild':
                        ans = str(input('What color would you like to play?\n'))
                        new_color = 'card ' + ans
                        change = True
                        break

                    elif next_card == '\n':
                        print("\nPlease input a card or draw\n")

                    elif next_card not in player2_hand.cards:
                        print("\nThis card is not in your hand\n")

                    else:
                        break


                check2 = Check(next_card)
                #Check for Skip
                if check2.skip() == True:
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = True
                    player1 = False
                    if win(player2_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                #Check for Reverse
                elif check2.reverse() == True:
                    
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = True
                    player1 = False
                    reverse = False
                    if win(player2_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break


                else:
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = False
                    player1 = True
                    if win(player2_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

            #If not active continue with original rotation
            else:

                #Check for a draw4 or a draw2 card
                check = Check(card_played)
                check.draw4(player2_hand)
                check.draw2(player2_hand)


                while True:

                    print('\n'*100)
                    if change == True:
                        card_played = new_color
                        print('Card in play: ' + card_played + '\n')
                        change = False
                    else:
                        print('Card in play: ' + card_played + '\n')

                    print('player 2 cards: \n')
                    show_cards(player2_hand)
                    try:
                        next_card = str(input('\nWhich card would you like to play? Or type Draw.\n'))

                    except TypeError:
                        print("\nPlease input a card or draw\n")

                    if next_card.lower() == 'draw':
                            player2_hand.add_card(deck.deal())

                    elif next_card.split()[0] == 'draw_4' or next_card.split()[0] == 'wild':
                        ans = str(input('What color would you like to play?\n'))
                        new_color = 'card ' + ans
                        change = True
                        break

                    elif next_card == '\n':
                        print("\nPlease input a card or draw\n")

                    elif next_card not in player2_hand.cards:
                        print("\nThis card is not in your hand\n")

                    else:
                        break


                check2 = Check(next_card)
                #Check for Skip
                if check2.skip() == True:
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = True
                    player1 = False
                    if win(player2_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

                #Check for Reverse
                elif check2.reverse() == True:
                    
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = True
                    player1 = False
                    reverse = True
                    if win(player2_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break


                else:
                    remove_check = player2_hand.remove_card(next_card, card_played)
                    if remove_check == True:
                        
                        index = player2_hand.cards.index(next_card)
                        player2_hand.cards.remove(player2_hand.cards[index])
                        card_played = next_card
                    else:
                        print("card can't be played\n")
                        continue

                    player2 = False
                    player1 = True
                    if win(player_hand.cards) == True:
                        print('Player 2 Wins!')
                        player1 = False
                        player2 = False
                        game_playing = False
                    break

    while True:
        try:
            contin = str(input('Would you like to play again? Enter Yes or No\n'))
            if contin.lower() == 'yes':
                game_con = True
                break

            elif contin.lower() == 'no':
                game_con = False
                break

        except TypeError:
            print('Please Enter Yes or No.\n')

    


