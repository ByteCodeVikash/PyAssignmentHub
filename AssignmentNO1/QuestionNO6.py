"""
Q6. Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points)

"""

game_played=int(input("Enter the number of game played: "))
game_won=int(input("Enter the number of game won:  "))
game_loss=int(input("Enter the number of game loss: "))

game_tied=game_played-game_won-game_loss

total_point=(game_won*4)+(game_tied*2)

print(f"Number of ties: {game_tied}")
print(f"Total point: {total_point}")


