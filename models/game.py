class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def draw(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return "It's a draw, better luck next time"
        
    def winner(self, player_1, player_2):
        if (player_1.choice == "Rock" and player_2.choice == "Scissors") or (player_1.choice == "Paper" and player_2.choice == "Rock") or (player_1.choice == "Scissors" and player_2.choice == "Paper"):
            return player_1.name() + "Wins"
        else:
            return player_2.name() + "Wins"



