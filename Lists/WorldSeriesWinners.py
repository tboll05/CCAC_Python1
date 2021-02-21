#Connect to text file
infile = open('WorldSeriesWinners.txt','r')

#Read the lines in the text file in to a list
teams = []

for line in infile:
    line = line.rstrip('\n')
    teams.append(line)

#User enters the name of a team
searchedTeam = input("Enter the name of a team: \n")

#Count the number of times this team shows up on the list
count = teams.count(searchedTeam)

#Print output
print("The", searchedTeam, "won the world series", str(count), "times between 1903 and 2009.")