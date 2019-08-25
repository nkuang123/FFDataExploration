# This script will acquire ADP (average draft position) data from 
# fantasyfootballcalculator.com in the JSON format and pack
# it nicely into a pandas DataFrame

import requests
from pandas.io.json import json_normalize

# credentials such as API keys
api_key = '92e098a7ea214119970b5e4c72ce465c'

# fantasyfootballcalculator.com customizable parameters
# when making an API request

scoring_format = 'standard'  # standard or ppr
num_of_teams = '10'  
year = '2019'
position = 'all'  # possible positions ['all', 'QB', 'RB', 'WR', 'TE', 'PK', 'DEF']


# retrieving ADP data from fantasyfootballcalculator.com
adp_response = requests.get("https://fantasyfootballcalculator.com/api/v1/adp/{}?teams={}&year={}&position={}". \
	format(scoring_format, num_of_teams, year, position))

# retrieving 2018 regular season player statistics from sportsdata.io 
sd_response = requests.get("https://api.sportsdata.io/v3/nfl/scores/json/Players?key={}". \
	format(api_key))

# convert to JSON
sd_json = sd_response.json()
adp_json = adp_response.json()

# we're only concerned with player data
players = adp_json['players']

df = json_normalize(adp_json, 'players')

# let's create a mapping 
name_to_id_dict = {player['name']: 0 for player in players} 

# mapping player names to player IDs
# data still needs to be cleaned i.e. Pat Mahomes != Patrick Mahomes
# for player in sd_json:
# 	player_name = player['FirstName'] + " " + player['LastName']
# 	if player_name in name_to_id_dict:
# 		name_to_id_dict[player_name] = player['PlayerID']


df = json_normalize(adp_json, 'players')

