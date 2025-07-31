import numpy as np
from game_environment import BlackJackEnv

epochs = 500000
initial_epsilon = 1.0
min_epsilon = 0.05
epsilon_decay = 0.99995

alpha = 0.2
gamma = 0.8

q_table = np.zeros((22, 12, 2, 2))
env = BlackJackEnv()
epsilon = initial_epsilon

for epoch in range(epochs):
    player_score, dealer_card, usable_ace = env.reset_game()
    usable_ace = int(usable_ace)
    game_over = False

    while not game_over:
        if np.random.rand() < epsilon:
            action = np.random.choice([0, 1])
        else:
            action = np.argmax(q_table[player_score, dealer_card, usable_ace, :])

        next_state, reward, game_over, _ = env.step(action)
        next_player_score, next_dealer_card, next_usable_ace = next_state
        next_usable_ace = int(next_usable_ace)

        next_score, _ = env.calculate_hand(env.player_hand)
        if next_score > 21:
            next_max = 0
        else:
            next_max = np.max(q_table[next_player_score, next_dealer_card, next_usable_ace, :])

        old_value = q_table[player_score, dealer_card, usable_ace, action]
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[player_score, dealer_card, usable_ace, action] = new_value

        player_score = next_player_score
        dealer_card = next_dealer_card
        usable_ace = next_usable_ace

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

np.save('q_table.npy', q_table)
print("Eğitim tamamlandı.")
