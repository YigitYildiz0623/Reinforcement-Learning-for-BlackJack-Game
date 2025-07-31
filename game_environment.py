import random

class BlackJackEnv():
    
    def __init__(self):
        self.card_deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.player_hand = []
        self.dealer_hand = []

    def draw_card(self):
        return random.choice(self.card_deck)

    def calculate_hand(self, hand):
        values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
        score = 0
        ace_count = 0

        for card in hand:
            if card == 'A':
                ace_count += 1
            score += values[card]

        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1

        usable_ace = True if 'A' in hand and score + 10 <= 21 else False
        return score, usable_ace

    def dealer_hand_value(self, card):
        if card in ['J','Q','K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    def get_state(self):
        player_score, usable_ace = self.calculate_hand(self.player_hand)
        dealer_card = self.dealer_hand_value(self.dealer_hand[0])
        return (player_score, dealer_card, usable_ace)

    def reset_game(self):
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        return self.get_state()

    def reward(self):
        player_score, _ = self.calculate_hand(self.player_hand)
        dealer_score, _ = self.calculate_hand(self.dealer_hand)

        if player_score > 21:
            return -1
        elif dealer_score > 21:
            return 1
        elif player_score > dealer_score:
            return 1
        elif player_score == dealer_score:
            return 0
        else:
            return -1

    def step(self, action):
        if action == 0:
            while self.calculate_hand(self.dealer_hand)[0] < 17:
                self.dealer_hand.append(self.draw_card())
            next_state = self.get_state()
            reward = self.reward()
            done = True
            return next_state, reward, done, self.player_hand

        elif action == 1:
            self.player_hand.append(self.draw_card())
            player_score, usable_ace = self.calculate_hand(self.player_hand)
            if player_score > 21:
                return self.get_state(), -1, True, self.player_hand
            else:
                return self.get_state(), 0, False, self.player_hand
