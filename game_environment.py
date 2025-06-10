import random

class BlackJackEnv():
    
    def __init__(self):
        self.card_deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.player_hand = []
        self.dealer_hand = []

    def draw_card(self):
        return random.choice(self.card_deck)
    
    
    def calculate_hand(self,hand):
        values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
        score = sum(values[card] for card in hand)

        if 'A' in hand and score>21:
            score -= 10

        return score
    
    def dealer_hand_value(self,card):
        if card in ['J','Q','K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    
    def get_state(self):
        return (self.calculate_hand(self.player_hand), self.dealer_hand_value(self.dealer_hand[0]))
    
    def reset_game(self):
        self.player_hand = [self.draw_card(),self.draw_card()]
        self.dealer_hand = [self.draw_card(),self.draw_card()]
        return self.get_state()
    
    def reward(self):
        player_score = self.calculate_hand(self.player_hand)
        dealer_score = self.calculate_hand(self.dealer_hand)

        if player_score > 21:
            return -1  # Oyuncu patladı, kayıp
        elif player_score >= 15 and len(self.player_hand) > 2:
            return -0.5  # 17 ve üstünde fazla kart çekmek riskli, ceza ver
        elif dealer_score > 21 or player_score > dealer_score:
            return 1  # Oyuncu kazandı
        elif player_score == dealer_score:
            return 0  # Berabere
        else:
            return -1  # Kaybetti


    def step(self,action):
        # Action -> 0 = Dur  |  Action -> 1 = Çek
        if action == 0:
            while self.calculate_hand(self.dealer_hand) <17:
                self.dealer_hand.append(self.draw_card())
            
            return self.get_state(), self.reward(), True,self.player_hand
        
        elif action == 1:
            self.player_hand.append(self.draw_card())
            
            if self.calculate_hand(self.player_hand) >21:
                return self.get_state(), -1, True,self.player_hand #Patladık
            else:
                return self.get_state(), 0, False,self.player_hand #Oyuna Devam
            