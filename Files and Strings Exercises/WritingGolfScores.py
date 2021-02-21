file = open('golf.txt', 'w')

numPlayers = int(input("Enter the number of players in the tournament: \n"))

for i in range(numPlayers):
    file.write(input("Enter the name of the player: \n"))
    file.write(input("Enter the golf score: \n"))

file.close()