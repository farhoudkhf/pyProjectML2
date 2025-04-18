# 5 dice rolls between 2 players 
import time
import numpy as np

d1 = [] 
d2 = []
player1Point = []
player2Point = []
player1PointTotal = 0
player2PointTotal = 0

for i in range(9, -1, -1):
    dice1 = np.random.randint(low=1, high=7)
    dice2 = np.random.randint(low=1, high=7)
    diceRollTotal = dice1 + dice2
    if i%2 != 0:
        player1PointTotal += (diceRollTotal)
        player1Point.append(diceRollTotal)
    else:
        player2PointTotal += (diceRollTotal)
        player2Point.append(diceRollTotal)
    playerNum = "P_One" if i%2 != 0 else "P _ Tow _ "
    print(f'{playerNum}_roll{i+1}: {dice1}, {dice2}, total: {diceRollTotal}, runningTotal: {player1PointTotal if playerNum == "P_One" else player2PointTotal}')
    time.sleep(0.4)
    d1.append(dice1)
    d2.append(dice2)

# print("dice1: ", d1, "dice2: ", d2)
print("player1Point total: ", player1Point)
print("player2Point total: ", player2Point)
print("Player One is the winner!" if player1PointTotal > player2PointTotal else "Player Two is the winner!" if player2PointTotal > player1PointTotal else "tie / equal score")
