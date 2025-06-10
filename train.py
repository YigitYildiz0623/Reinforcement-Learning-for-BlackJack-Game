import numpy as np
from game_environment import BlackJackEnv

#HiperParametreler
epochs = 500000 # Eğitim sayısı



alpha = 0.3  # Öğrenme oranı(Learning_rate)
gamma = 0.9  # İndirim faktörü
epsilon = 0.8  # Keşif oranı

q_table = np.zeros((22, 12, 2))
env = BlackJackEnv()

for epoch in range(epochs):
    state = env.reset_game()
    game_over = False

    while not game_over:
        player_score, dealer_hand = state
        if np.random.rand() < epsilon:
            action = np.random.choice([0,1]) #Rastgele eylem(Keşif)
        else:
            action = np.argmax(q_table[player_score, dealer_hand]) #En iyi eylem

        next_state, reward, game_over,_ = env.step(action)
        next_player_score, next_dealer_hand = next_state

        old_value = q_table[player_score, dealer_hand, action]
        if next_player_score >= 22:  
             next_max = 0  # Patladıysa gelecek ödül 0 olmalı  
        else:  
            next_max = np.max(q_table[next_player_score, next_dealer_hand])
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max) #Balmer Denklemi
        q_table[player_score, dealer_hand, action] = new_value

        state = next_state

np.save('q_table.npy',q_table)
print('Eğitim Tamamlandı')