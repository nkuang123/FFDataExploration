import sqlite3
import json
import pandas as pd
from pandas.io.json import json_normalize
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)


def create_stats_dataframe() -> pd.DataFrame:
	# Sportsdata.io API URL for 2018 Regular Season Player Stats:
	# https://api.sportsdata.io/v3/nfl/stats/json/PlayerSeasonStats/2018REG
	# ?key=92e098a7ea214119970b5e4c72ce465c
	# 
	# Because it is an expensive API call, we'll save the results to a local JSON 
	# repository.
	stats_json = os.path.join(parent_dir, 'json', '2018REG.json')

	with open(stats_json) as regular2018_json:
		data = json.load(regular2018_json)  # deserialize json file

	# Debugging & confirmation print statements
	# 
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

	stats_df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
	stats_df = stats_df.drop(columns=['ScoringDetails'])

	return stats_df