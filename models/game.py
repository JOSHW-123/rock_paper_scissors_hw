class Game:
    def __init__(self):
        self.win_dict = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def play(self, player_1, player_2):
    
        winner = None

        if self.win_lookup[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.win_lookup[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner
   
        

    # def draw(self, player_1, player_2):
    #     if player_1.choice == player_2.choice:
    #         return "It's a draw, better luck next time"
        
    # def winner(self, player_1, player_2):
    #     if (player_1.choice == "Rock" and player_2.choice == "Scissors") or (player_1.choice == "Paper" and player_2.choice == "Rock") or (player_1.choice == "Scissors" and player_2.choice == "Paper"):
    #         return player_1.name + ("Wins")
    #     else:
    #         return player_2.name + ("Wins")



