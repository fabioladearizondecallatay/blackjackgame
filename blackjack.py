import random

#el dicionario de cartas
cards = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

def create_deck():
#para crear la baraja de cartas repitiendo las claves del dicionario 4veces
    deck = list(cards.keys()) * 4  #se usan 4 cartas
    random.shuffle(deck)
    return deck

def shuffle_deck():
#funcion para mezclar las cartas restantes
    deck = create_deck()
    random.shuffle(deck)
    return deck

def hand_value(hand):
#funcion para calcular el valor de las cartas (sumando)
    value = sum(cards[card] for card in hand)
    
    #ajuste para el as que tiene doble valor
    aces = hand.count(chr(0x1f0a1))
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def play_blackjack():
#funcion principal para jugar al juego 
    print("Welcome to Blackjack!")

#se reparten dos cartas al jugador y dos al dealer 
    deck = shuffle_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

#muestra los valores iniciales del jugador la carta visualizada del dealder
    print("\nYour hand:", player_hand, "  Value:", hand_value(player_hand))
    print("Dealer's cards:", dealer_hand[0], " and a hidden card.")

    #el jugador recibe dos cartas y decide si quiere pedir una mas o mantener su mano
    for _ in range(2):
        action = input("Do you want to 'Hit' or 'Stand'? ").lower()
        if action == 'hit':
            new_card = deck.pop()
            player_hand.append(new_card)
            print("You received the card:", new_card)
        elif action == 'stand':
            break
        else:
            print("Please choose 'Hit' or 'Stand'.")

    #el dealer coje carta si tiene una mano debajo del 17
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    #para que aparezca el valor final del dealer y del jugador
    print("\nDealer's hand:", dealer_hand, "  Value:", hand_value(dealer_hand))
    print("Your hand's value:", hand_value(player_hand))

    #resultado del juego 
    if hand_value(player_hand) > 21:
        print("YOU LOST, you're busted...")
    elif hand_value(dealer_hand) > 21:
        print("YOU WON! The dealer's busted!")
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("YOU WON! Your hand is better than the dealer's!!!")
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("YOU LOST, the dealer's hand is better...")
    else:
        print("It's a tie.")

#para determinar que le script se ejecuta como programa principal
if __name__ == "__main__":
    play_blackjack()
