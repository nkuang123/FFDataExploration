from acquire_player_stats import create_stats_dataframe
from acquire_data import create_adp_dataframe
import requests
import json
import sqlite3

# Establish connection to database
conn = sqlite3.connect('FantasyFootballDB.db')
c = conn.cursor()

# Fantasyfootballcalculator.com customizable parameters when making an API 
# request. Adjust based on your league settings.
scoring_format = 'standard'  # Standard or PPR scoring
num_of_teams = '10'  # 10, 12, 14 teams
year = '2019'
position = 'all'  # Possible positions: ['all', 'QB', 'RB', 'WR', 'TE', 
				  # 'PK', 'DEF']

# Retrieve DataFrames
adp_df = create_adp_dataframe(scoring_format, num_of_teams, year, position)
stats_df = create_stats_dataframe()

# Need to clean up DataFrames before creating tables in the database.
# Specifically, we need to create a sportsdata_id section in the ADP 
# DataFrame in order to join it with the stats DataFrame for analysis 
# and processing.
def insert_playerID_column(adp_dataframe):
	# We need to shorten the names in the ADP DataFrame since that is how
	# names are recorded in the stats DataFrame. To deal with multiple 
	# players with the same short name, we'll also need to note the 
	# players' team. A dictionary mapping will suffice.

	# retrieving 2018 REG season player profile info from sportsdata.io 
	with open('.secret/credentials.json') as f:
		params = json.load(f)
		api_key = params['api_key']
		url = "https://api.sportsdata.io/v3/nfl/scores/json/Players?key={}" \
			.format(api_key)
		sportsdata_response = requests.get(url)

	# let's create a mapping 
	name_to_id_dict = {player: None for player in adp_dataframe['name'].values} 

	# mapping player names to player IDs
	# data still needs to be cleaned i.e. Pat Mahomes != Patrick Mahomes
	for player in sportsdata_response.json():
		player_name = player['FirstName'] + " " + player['LastName']
		if player_name in name_to_id_dict:
			name_to_id_dict[player_name] = player['PlayerID']

	# adding player IDs
	c.execute('ALTER TABLE PLAYERS ADD COLUMN sportsdata_id INTEGER')

	for name in name_to_id_dict:
	    c.execute('UPDATE PLAYERS SET sportsdata_id = ? WHERE name = ?', \
	    	(name_to_id_dict[name], name))

	conn.commit()

# Create the sportsdata_id column
insert_playerID_column(adp_df)