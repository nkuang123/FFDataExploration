# This script will acquire ADP (average draft position) data from 
# fantasyfootballcalculator.com in the JSON format and pack
# it nicely into a pandas DataFrame.
import requests
import pandas as pd
from pandas.io.json import json_normalize

def create_adp_dataframe(
	scoring_format: str,
	num_of_teams: str,
	year: str,
	position: str) -> pd.DataFrame:


	url = '''https://fantasyfootballcalculator.com/api/v1/adp/standard?teams=
		10&year=2019&pos=all''' \
		.format(scoring_format, num_of_teams, year, position)

	# Retrieving ADP data from fantasyfootballcalculator.com
	adp_response = requests.get(url)

	# retrieving 2018 regular season player statistics from sportsdata.io 
	# sd_response = requests.get("https://api.sportsdata.io/v3/nfl/scores/json/Players?key={}". \
	# 	format(api_key))

	# Convert to JSON format
	adp_json = adp_response.json()

	# We're only concerned with player data
	players = adp_json['players']

	# df = json_normalize(adp_json, 'players')
	return pd.DataFrame.from_dict(json_normalize(adp_json, 'players'))


