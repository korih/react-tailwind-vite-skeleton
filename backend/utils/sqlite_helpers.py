import sqlite3
import json

sql_file_path = "./models/leaderboard.sql"
populate_sql_path = "./models/populate_leaderboard.sql"
db_file = "./models/leaderboard.db"

def init_db():
	"""
	Create the leaderboard table if it does not exist
	"""
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		with open(sql_file_path, 'r') as sql_file:
			sql_script = sql_file.read()
			cursor.executescript(sql_script)

	except Exception as e:
		print("Error in init_db:")
		print(e)
	finally:
		connection.close()

def get_all_rows() -> str:
	"""
	Returns a str representing all the columns in JSON format
	"""
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT * FROM leaderboard;")
		rows = cursor.fetchall()
		column_names = [description[0] for description in cursor.description]
		data = [dict(zip(column_names, row)) for row in rows]
		json_data: str = json.dumps(data, indent=4)
		return json_data
	except Exception as e:
		print("Error in populate_db, raising error")
		raise e
	finally:
		connection.close()

def add_row(name: str, score: int):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO leaderboard(name, score) VALUES (?, ?);", [name, score])
		connection.commit()
	except Exception as e:
		print("Error in add_row, raising error")
		raise e
	finally:
		connection.close()

def remove_row(id: int):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		cursor.execute("DELETE FROM leaderboard WHERE id = ?;", (id, ))
		connection.commit()
	except Exception as e:
		print("Error in remove_row, raising error")
		raise e
	finally:
		connection.close()

def update_row(id: int, new_score: int):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		cursor.execute("UPDATE leaderboard SET score = ? WHERE id = ?;", (new_score, id))
		connection.commit()
	except Exception as e:
		print("Error in update_row, raising error")
		raise e
	finally:
		connection.close()
