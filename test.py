import numpy as np
from game_environment import BlackJackEnv

q_table = np.load('q_table.npy')
env = BlackJackEnv()

num_test = 10000
wins = 0
loses = 0
draws = 0

for _ in range(num_test):
    player_score, dealer_card, usable_ace = env.reset_game()
    usable_ace = int(usable_ace)
    game_over = False

    while not game_over:
        action = np.argmax(q_table[player_score, dealer_card, usable_ace, :])
        next_state, reward, game_over, _ = env.step(action)
        player_score, dealer_card, usable_ace = next_state
        usable_ace = int(usable_ace)

    if reward == 1:
        wins += 1
    elif reward == -1:
        loses += 1
    else:
        draws += 1

win_rate = wins / num_test
lose_rate = loses / num_test
draw_rate = draws / num_test

print('Testler Bitti')
print('-')
print(f'Kazanma Sayısı: {wins}  -   Kaybetme Sayısı: {loses} -   Beraberlik Sayısı: {draws}')
print(f'Kazanma Oranı: {win_rate * 100:.2f}%    Kaybetme Oranı: {lose_rate * 100:.2f}%    Beraberlik Oranı: {draw_rate * 100:.2f}%')
