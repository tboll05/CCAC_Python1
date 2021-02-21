infile = open('WorldSeriesWinners.txt','r')

teams = []

for line in infile:
    line = line.rstrip('\n')
    teams.append(line)

num_wins_dict = {}

for team in teams:
    if team in num_wins_dict.keys():
        num_wins_dict[team] +=1
    else:
        num_wins_dict[team] = 1
        
#Create a dictionary where the key is the year and the value is the name of the team that won that year
years_dict = {}

index = 0

for year in range(1903,2009):
    if year == 1904 or year == 1994:
        continue
    else:
        years_dict[year] = teams[index]
        index +=1
        
user_entry = int(input("Enter a year in the range 1903-2009: \n"))

if user_entry == 1904 or user_entry == 1994:
    print("The world series wasn't played in the year " + str(user_entry))
else:
    print(f"The team that won the world series in {user_entry} is the " + years_dict[user_entry] + ".")
    print("They won the world series " + str(num_wins_dict[years_dict[user_entry]]) + " times.")