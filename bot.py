import numpy as np

# Eğitilmiş Q-table'ı yükle
q_table = np.load("q_table.npy")

continue_game = True

def get_action(player_score, dealer_card):
    
    action = np.argmax(q_table[player_score, dealer_card])
    if action == 1:
        return "Hit (Kart Çek)",1
    else:
        return "Stand (Bekle)",2

while continue_game == True:
    try:
        player_score = int(input("Oyuncunun toplam puanını gir (0-21): "))
        dealer_card = int(input("Krupiyenin açık kartını gir (1-11): "))

        bot_action = get_action(player_score,dealer_card)
        
        if bot_action[1] == 1:
            print(bot_action[0])
            new_card = int(input("Oyuncunun yeni kartını girin: "))
            player_score += new_card
        
            if player_score>21:
                print("Kaybedildi")
            else:
                bot_action = get_action(player_score,dealer_card)

                if bot_action[1] == 1:
                    print(bot_action[0])
                    new_card = int(input("Oyuncunun yeni kartını girin: "))
                    player_score += new_card
        
                    if player_score>21:
                        print("Kaybedildi")
                
                else:
                    print(bot_action[0])
        
        else:
            print(bot_action[0])

        game_opt = input("Oyuna devam edilsin mi? (y/N)").lower()

        if game_opt == "y":
            pass
        else:
            print("Bot Durduruldu")
            continue_game = False

    except ValueError:
        print("Lütfen geçerli bir sayı gir!")
