import sqlite3

# create connection to database stored (or to be created) in file 'music.sqlite'
conn = sqlite3.connect('music.sqlite')
# cursor is a pointer to the db file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# |-----------------------------|
# |			Tracks 				|
# |-----------------------------|
# |title(TEXT)	|plays(INTEGER)	|
# |-----------------------------|
# |data			|data			|
# |-----------------------------|

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
	('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
	('My Way', 15))
# commit to force writting to db file
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
for row in cur:
	print(row)

# select all (*) columns for rows with title 'My Way'
cur.execute('SELECT * FROM Tracks WHERE title = "My Way"')
for row in cur:
	print(row)

cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "My Way"')
# we only need to commit to write to disk
cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
for row in cur:
	print(row)


cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

conn.close()