import sqlite3
import json
import pandas as pd
from pandas.io.json import json_normalize

conn = sqlite3.connect('FantasyFootballDB.db')
c = conn.cursor()

# fetch all player names and their player IDs, exclude Defenses
sql_players = c.execute('''SELECT name, sportsdata_id FROM PLAYERS
	WHERE position NOT IN ('DEF')''')

player_dict = {}

for player in sql_players:
	name, sportsdata_id = player
	player_dict[sportsdata_id] = name

# reading in player stats for the 2018 regular season as a json file
with open('json/2018REG.json') as regular_2018_json:
	data = json.load(regular_2018_json)
	# print(data[0].keys())
	# print("{:18} | {:15} | {:15} | {:15} | {:15} | {:15} | {:15} | {:15}".format("Name", \
	# 	"Pass Attempts", "Pass Yards", "Pass Comp. %", \
	# 	"Pass YPA", "Pass YPC", "Pass TDs", "Pass Rating"))
	# for player in data:
	# 	if player['Position'] == 'QB' and player['PlayerID'] in player_dict:  # player is an RB
	# 		print("{:18} | {:15} | {:15} | {:15} | {:15} | {:15} | {:15} | {:15}".format(\
	# 			player['Name'], player['PassingAttempts'], player['PassingYards'], \
	# 			player['PassingCompletionPercentage'], player['PassingYardsPerAttempt'],\
	# 			player['PassingYardsPerCompletion'], player['PassingTouchdowns'], \
	# 			player['PassingRating']))

# convert json data to DataFrame for ease 
stat_df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')

stat_df = stat_df.drop(columns=['ScoringDetails'])

# let SQL deal with filtering
# only concerned with players in ADP rankings
# filtered_df = stat_df[stat_df['PlayerID'].isin(player_dict.keys())]

# # remove unnecessary columns/statistics
# filtered_df = filtered_df.drop(columns=['ScoringDetails'])

# print(filtered_df.filter(['PlayerID', 'Team', 'Name', 'PassingYards', 'PassingTouchdowns', \
# 	'PassingRating', 'RushingAttempts', 'RushingYards', 'RushingTouchdowns']).to_string())


# print(filtered_df['PlayerID'])

#print(player_dict)