from app import app
from flask import render_template
import os
from app.models import QBTable, RBTable, WRTable, TETable
from app.stats_2018_reg_model import FootballStats_DB

def get_database():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	parent_dir = os.path.dirname(current_dir)
	db_file = os.path.join(parent_dir, 'scripts', 'FantasyFootballDB.db')

	db = FootballStats_DB(db_file)

	return db

# Home Page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

# Quarterback Information
@app.route('/quarterbacks')
def quarterbacks_page():
	fb_db = get_database()

	items = [row for row in fb_db.get_qbs().itertuples()]
	table = QBTable(items)

	return render_template(table.__html__())

# Running Back Information
@app.route('/runningbacks')
def runningbacks_page():
	fb_db = get_database()

	items = [row for row in fb_db.get_rbs().itertuples()]
	table = RBTable(items)

	return table.__html__()

# Wide Receiver Information
@app.route('/widereceivers')
def widereceivers_page():
	fb_db = get_database()

	items = [row for row in fb_db.get_wrs().itertuples()]
	print(fb_db.get_wrs())
	table = WRTable(items)

	return table.__html__()

# Tight End Information
@app.route('/tightends')
def tightends_page():
	fb_db = get_database()

	items = [row for row in fb_db.get_tes().itertuples()]
	print(fb_db.get_tes())
	table = TETable(items)

	return table.__html__()
