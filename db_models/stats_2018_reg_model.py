import sqlite3
import pandas as pd

class FootballStats_DB:

	scramble_factor = 1.392

	# create a connection to the stats database
	def __init__(self):
		self.conn = sqlite3.connect('FantasyFootballDB.db')  # establish connection
		self.c = self.conn.cursor()


	def get_qbs(self, order_by='PassingYards'):
		query = '''
			SELECT Name, CAST(ROUND(PassingAttempts/{}) AS INT) AS PassAttempts, 
			CAST(ROUND(PassingYards/{}) AS INT) AS PassYards, 
			CAST(ROUND(PassingTouchdowns/{}) AS INT) AS PassTouchdowns
			FROM STATS2018REG
			WHERE Position LIKE "QB"
			ORDER BY {} DESC'''.format(self.scramble_factor, self.scramble_factor, self.scramble_factor, order_by)
		return pd.read_sql(query, self.conn)


	def get_rbs(self, order_by='RushingYards'):
		query = '''
			SELECT Name, 
			CAST(ROUND(RushingAttempts/{}) AS INT) AS RushAttempts, 
			CAST(ROUND(RushingYards/{}) AS INT) AS RushYards, 
			CAST(ROUND(RushingTouchdowns/{}) AS INT) AS RushTouchdowns
			FROM STATS2018REG
			WHERE Position LIKE "RB"
			ORDER BY {} DESC'''.format(self.scramble_factor, self.scramble_factor, self.scramble_factor, order_by)
		return pd.read_sql(query, self.conn)

	def get_wrs(self, order_by='ReceivingYards'):
		query = '''
			SELECT Name, CAST(ROUND(Receptions/{}) AS INT) AS Receptions, 
			CAST(ROUND(ReceivingYards/{}) AS INT) AS ReceivingYards, 
			CAST(ROUND(ReceivingTouchdowns/{}) AS INT) AS ReceivingTouchdowns
			FROM STATS2018REG
			WHERE Position LIKE "WR"
			ORDER BY {} DESC'''.format(self.scramble_factor, self.scramble_factor, self.scramble_factor, order_by)
		return pd.read_sql(query, self.conn)

	def get_tes(self, order_by='ReceivingYards'):
		query = '''
			SELECT Name, CAST(ROUND(Receptions/{}) AS INT) AS Receptions, 
			CAST(ROUND(ReceivingYards/{}) AS INT) AS ReceivingYards, 
			CAST(ROUND(ReceivingTouchdowns/{}) AS INT) AS ReceivingTouchdowns
			FROM STATS2018REG
			WHERE Position LIKE "WR"
			ORDER BY {} DESC'''.format(self.scramble_factor, self.scramble_factor, self.scramble_factor, order_by)
		return pd.read_sql(query, self.conn)

	def get_kickers(self):
		self.c.execute('''
			SELECT Name 
			FROM STATS2018REG
			WHERE Position LIKE "K"''')
		print(self.c.fetchall())


	def get_adp_players(self):
		query = '''
			SELECT Name, CAST(ROUND(PassingAttempts/{}) AS INT) AS PassAttempts, 
			CAST(ROUND(PassingYards/{}) AS INT) AS PassYards, 
			CAST(ROUND(PassingTouchdowns/{}) AS INT) AS PassTouchdowns,
			CAST(ROUND(RushingAttempts/{}) AS INT) AS RushAttempts, 
			CAST(ROUND(RushingYards/{}) AS INT) AS RushYards, 
			CAST(ROUND(RushingTouchdowns/{}) AS INT) AS RushTouchdowns,
			CAST(ROUND(Receptions/{}) AS INT) AS Receptions, 
			CAST(ROUND(ReceivingYards/{}) AS INT) AS ReceivingYards, 
			CAST(ROUND(ReceivingTouchdowns/{}) AS INT) AS ReceivingTouchdowns
			FROM STATS2018REG
			WHERE PlayerID IN (SELECT sportsdata_id FROM PLAYERS)
		'''.format(
			self.scramble_factor, self.scramble_factor, self.scramble_factor,
			self.scramble_factor, self.scramble_factor, self.scramble_factor,
			self.scramble_factor, self.scramble_factor, self.scramble_factor)
		return pd.read_sql(query, self.conn)
