import pandas as pd
import numpy as np

# Tic Tac Toe 
# Board - 3 x 3 - Adjustable 
# Players - 2 
# Win condition is 3 in a row

class TicToe():

    def __init__(self, name, player, player_score, player_level, player_move):
        # Initilize Player Variables
        self.name = name 
        self.player = player
        self.player_score = player_score
        self.player_level = player_level
        self.player_move = player_move 

    def set_player(self):
        # Format the player name
        player = f"Player{self.player} {self.name}"
        return player 


class grid(TicToe):

    def __init__(self, size, player, player_move):
        self.size = size

    super.__init__(TicToe, player, player_move)
    # Create Grid Size
    def create_size(self):
        while True:
            try:
                size = int(input("Enter Size of Grid: 3, 9, 12, etc: ")) # Check if multiple of 3
                if size % 3 == 0:
                    break
                else:
                    print("Size Needs To Be a Multple of 3: 3, 6, 9, etc")

            except ValueError:
                print("Enter a Number")

        return size

        # Create the table using pandas
        def create_grid(self, size):
            size.create_size(size)
            li = {i:k for i,k in enumerate(grid.size)}
            box_grid = pd.DataFrame(li)
            return box_grid
        
    
# Outputting Player Names
list_of_players = []
for i in range(1,3):
    name = input(f"Player{i} Enter Your Name: ")
    play = TicToe(name, i, None, None, None)
    list_of_players.append(play.set_player())

# Output name in suitable format
print(f"\n{list_of_players[0]}\n{list_of_players[1]}") 

# Creation of Grid
box = grid(0)
box = box.create_grid(box.size)
print(box)
