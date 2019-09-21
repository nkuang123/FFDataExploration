from flask_table import Table, Col

class QBTable(Table):
	# Index = Col('Index')
	Name = Col('Name')
	PassAttempts = Col('Pass Attempts')
	PassYards = Col('Pass Yards')
	PassTouchdowns = Col('Pass TDs')

class RBTable(Table):
	Name = Col('Name')
	RushAttempts = Col('Rush Attempts')
	RushYards = Col('Rush Yards')
	RushTouchdowns = Col('Rush TDs')

class WRTable(Table):
	Name = Col('Name')
	Receptions = Col('Receptions')
	ReceivingYards = Col('Receiving Yards')
	ReceivingTouchdowns = Col('Receiving TDs')

class TETable(Table):
	Name = Col('Name')
	Receptions = Col('Receptions')
	ReceivingYards = Col('Receiving Yards')
	ReceivingTouchdowns = Col('Receiving TDs')