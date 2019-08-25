#from acquire_data import df
from acquire_player_stats import stat_df
from acquire_data import name_to_id_dict
import sqlite3
import pandas as pd

conn = sqlite3.connect('FantasyFootballDB.db')
c = conn.cursor()

# create player ADP database using a DataFrame; executed once during creation
# df.to_sql('PLAYERS', conn)

# create 2018 regular season player stat database using a DataFrame; executed once during creation

stat_df.to_sql('STATS2018REG', conn)

# adding player IDs
# c.execute('ALTER TABLE PLAYERS ADD COLUMN sportsdata_id INTEGER')

for name in name_to_id_dict:
	c.execute('UPDATE PLAYERS SET sportsdata_id = ? WHERE name = ?', (name_to_id_dict[name], name))


conn.commit()