import random

cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
game_play = {
    "y": True,
    "n": False,
}
to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while game_play[to_play]:
    def hit():
        card = player_card.append(random.choice(cards))
        if card == 11 and player_score > 10:
            return 1
        elif card == 11 and player_score <= 10:
            return 11
        return card


    def player_score_update(score=0):
        for i in player_card:
            score += i
        return score

    def computer_score_update(score=0):
        for i in computer_cards:
            score += i
        return score
    def final_cards():
        print(f"Your final hand: {player_card}, final score: {player_score}")
        print(f"Computer's final hand: , final score: {computer_score}")



    player_card = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    computer_score = computer_score_update()
    player_score = player_score_update()
    print(f"Your cards: {player_card} , current score: {player_score}")
    print(f"Computer's first card: {computer_cards}")

    while player_score <= 21:
        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_or_stand == "y":
            hit()
            player_score = player_score_update()
            print(f"Your cards: {player_card} , current score: {player_score}")
            print(f"Computer's first card: {computer_cards}")
        elif hit_or_stand == "n":
            break

    if player_score > 21:
        final_cards()
        print("You went over. You lose 😭")
        break
    else:
        while computer_score <= 17:
            computer_cards.append(random.choice(cards))
            computer_score = computer_score_update()

        if computer_score > 21:
            final_cards()
            print("Computer went over. You Win :) ")
            break
        else:
            if computer_score > player_score:
                final_cards()
                print("You lose 😤")
                break
            elif player_score > computer_score:
                final_cards()
                print("You win 😁")
                break
            else:
                final_cards()
                print("its a draw 🤝")
                break





