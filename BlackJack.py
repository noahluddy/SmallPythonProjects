from random import *

class Card(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Deck(object):
    def __init__(self):
        self.deck = []  ## Need self.
        for s in range(4):  ## s - suit
            for v in range(1, 14):  ## v - value
                self.deck.append(Card(v))
        ## Correcting for BlackJack
        for card in self.deck:
            if card.value > 10:
                card.value = 10

    def __str__(self):
        temp = []
        for card in self.deck:
            temp.append(str(card))
        return '  '.join(temp)

    def shuffle_deck(self):
        shuffle(self.deck)

    def get_card(self, i=-1):  ## The = in the parameter indicates default value that can be changed. -1 is the last element
        try:
            return self.deck.pop(i)  ## pop() is so cool
        except IndexError:
            print('No more cards in the deck! :(')
            quit()

class Player(object):
    def __init__(self, c1, c2, money):
        self.money = money
        self.cards = []
        self.cards.append(c1.value)
        self.cards.append(c2.value)
        self.sum = sum(self.cards)

    def add_card(self, c3):
        self.cards.append(c3.value)
        self.sum = sum(self.cards)

    def get_sum(self):
        return self.sum

    def blackjack(self):
        return (self.cards[0] == 1 and self.cards[1] == 10) or (self.cards[0] == 10 and self.cards[1] == 1)

    def make_bet(self, temp=-1):
        if temp == -1:
            bet = randint(1, self.money//2)
        else:
            bet = temp
        self.money -= bet
        return bet

    def win(self, winnings):
        self.money += int(winnings)

class Dealer(object):
    def __init__(self, c1):
        self.sum = 0
        self.sum += c1.value

    def add_card(self, c2):
        self.sum += c2.value

    def get_sum(self):
        return int(self.sum)

    def blackjack(self):
        return sum == 21

def play(deck_param, dealer_param, me_param):
    my_deck = deck_param
    my_deck.shuffle_deck()
    dealer = dealer_param
    me = me_param
    bet = me.make_bet()
    double = False
    print('\nYou bet: %i' % bet)
    print('Your stack is now: %i' % me.money)

    print('Dealer has a %i showing.' % int(dealer.sum))  ## I think both int(dealer.sum) and dealer.get_sum() work
    if 1 in me.cards:  ## If the player has an ace
        print('You have: %i/%i' %(me.get_sum(), me.get_sum()+10))
    else:
        print('You have: %i' % me.get_sum())

    if me.blackjack():
        print('Hooray! You win! BlackJack!')
        me.win(2.5*bet)  ## BlackJack extra
        end(me)

    '''
    if me.cards[0] == me.cards[1]:
        split = input('Would you like to split? (y/n)')
        if split == 'y':
            me2 = Player(me.cards[0], my_deck.get_card())
            me3 = Player(me.cards[1], my_deck.get_card())
    '''

    while me.sum < 21 and not double:
        hit = input('Would you like another card? (y/n) ')
        if hit == 'y':
            if len(me.cards) == 2:
                double_choice = input('Would you like to double down? (y/n) ')
                if double_choice == 'y':
                    double = True
                    me.make_bet(bet)
                    bet *= 2
                    print('Your stack is now: %i' % me.money)
            tmp1 = my_deck.get_card()
            me.add_card(tmp1)
            print('You got a %i' % tmp1.value)
            if 1 in me.cards and me.get_sum()+10 < 22:
                print('You now have: %i/%i' % (me.get_sum(), me.get_sum() + 10))
            else:
                print('You now have: %i' % me.get_sum())
        else:
            print('You stand.')
            break

    ## Correcting for Ace duplicity
    if 1 in me.cards and me.get_sum() + 10 < 22:
        me.sum += 10
        print('You now have: %i' % me.sum)

    '''
    Actually I can't do this because in real life if the player busts, the dealer doesn't take another card.
    dealer.add_card(my_deck.get_card()) ## Adding card here so I can use elif dealer.blackjack()
    '''

    if me.sum > 21:
        print('Sorry, you busted.')
        end(me)
        return

    dealer.add_card(my_deck.get_card())  ## Here is okay

    if dealer.blackjack():
        print('Dealer has BlackJack :(')
    else:
        print('Dealer starts with: %i' % dealer.sum)
        while dealer.sum < 17:  ## Dealer must hit on 16
            tmp2 = my_deck.get_card()
            dealer.add_card(tmp2)
            print('Dealer hits and gets a %i' % tmp2.value)
            print('Dealer now has: %i' % dealer.get_sum())
        if dealer.sum > 21 or dealer.sum < me.sum:
            if dealer.sum > 21:
                print('Dealer busted.')
            print('Hooray! You win!')
            me.win(2*bet)
        elif dealer.sum > me.sum:
            print('Sorry, you lost.')
        else:
            print('Push.')
            me.win(bet)  ## Really just getting the bet back
    end(me)  ## Make sure the end(me) is outside the else statement!

def end(me):
    print('Your stack is now: %i' % me.money)
    choice = input('Would you like to play again? (y/n) ')
    if choice == 'y':
        new_deck = Deck()
        new_deck.shuffle_deck()
        new_dealer = Dealer(my_deck.get_card())
        same_me = Player(my_deck.get_card(), my_deck.get_card(), me.money)  ## Keeps money the same
        play(new_deck, new_dealer, same_me)
    quit()  ## quit() needs to be here because of BlackJack calling end() early

my_deck = Deck()
my_deck.shuffle_deck()
dealer = Dealer(my_deck.get_card())
me = Player(my_deck.get_card(), my_deck.get_card(), 100)
play(my_deck, dealer, me)
