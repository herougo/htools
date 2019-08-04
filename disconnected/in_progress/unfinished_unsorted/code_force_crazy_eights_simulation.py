# unrefactored code due to power outage :|

import random
CARD_TYPES = list('A23456789JQK')
SUITS = 'Spades Hearts Clubs Diamonds'.split()
DECK_VALUES = [(card_type, suit) 
               for card_type in CARD_TYPES 
               for suit in SUITS]
            
class Pile:
    def __init__(self, values=None):
        if not values:
            self.data = []
        else:
            self.data = values
    
    def shuffle(self):
        random.shuffle(self.data)
        return self.data
    
    def draw_from_top(self, n=1):
        self.data, result = self.data[:-n], self.data[-n:]
        return result
        
    def add_to_top(self, values):
        self.data.extend(values)
        
    def reveal_top(self):
        return self.data[-1]
    
    def pop(self, i):
        return self.data.pop(i)
        
        
class Deck(Pile):
    def __init__(self):
        super(Deck, self).__init__(list(DECK_VALUES))
        

        
class Player:
    def __init__(self):
        self.hand = Pile()
        
class CrazyEightsGame:
    def __init__(self):
        self._log = []
        
    def _log_event(self, event):
        self._log.append(event)
        
    def _draw_cards(self, player_i, n=1):
        from_deck = min(n, len(self._deck))
        self._log_event('Player {} drew {} cards'.format(player_i, from_deck))
        cards = self._deck.draw_from_top(from_deck)
        if n - from_deck > 0:
            top = self._centre.draw_from_top()
            new_deck_cards = self._centre.draw_from_top(n - from_deck)
            self._deck.add_to_top(new_deck_cards)
            self._deck.shuffle()
            self._centre.add_to_top(top)
            self._log_event('Deck Reshuffled')
            
            cards.extend(self._deck.draw_from_top(n - from_deck))
            self._log_event('Player {} drew {} cards'.format(player_i, n - from_deck))
            
        self._player[player_i].hand.add_to_top(cards)
        
            
        
    def _is_playable(self, other_card):
        return (other_card[0] == '8' or 
                (self._top[0] == other_card[0]) or 
                (self._top[1] == other_card[1]))
        
    def _legal_card_plays(self, player):
        return [i for i in range(len(player.hand)) if self._is_playable(self._hand[i])]
        
    def _play_card(self, choice_card):
        type, suit = choice_card
        opp = 1 - self._turn
        if type == '2':
            player_i, self._draw_cards(n=2)
        elif type == '8':
            choices = list(range(4))
            random.shuffle(choices) # lazy
            suit = SUITS[choices[0]]
            self._top[1] = suit
            self._log_event('Suit {} Chosen'.format(suit))
        elif type == '4':
            self._turn = (self._turn + 1) % 2
            self._log_event('Player {} turn skipped'.format(self._turn))
            
        self._centre.add_to_top([choice_card])
            
        self._turn = (self._turn + 1) % 2
    
    def simulate_game(self):
        self._log = []
        
        # start
        self._deck = Deck().shuffle()
        self._players = [Player(), Player()]
        self._centre = Pile()
        self._top = None
        self._turn = 0
        
        # deal
        for player_i in [0, 1]:
            self._draw_cards(player_i, n=5)
        self._centre.add_to_top(self._deck.draw_from_top())
        self._top = self._centre.reveal_top()
        self._log_event('{} of {} Revealed'.format(self._top))
        
        
        while len(self._players[0].hand) > 0 and len(self._players[1].hand) > 0:
            player = self._players[self._turn]
            legal_card_plays = self._legal_card_plays(player)
            
            if len(legal_card_plays) == 0:
                player.add_to_top(self._draw_cards(n=1))
            else:
                choices = list(range(len(legal_card_plays)))
                random.shuffle(choices) # lazy
                choice_card = player.hand.pop(choices[0])
                self._play_card(choice_card)

        return self._log

log = CrazyEightsGame().simulate_game()
for line in log:
    print(log)
