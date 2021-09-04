import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

# function to print a set number of rows from a specified table in current db
def print_rows(table, rows):
	cur.execute('SELECT * FROM ' + table)
	count = 0
	print('People:')
	for row in cur:
		if count < rows: print(row)
		count += 1
	print(count, 'rows.')
	
print_rows('People', 5)
print_rows('Followers', 5)

cur.execute('''SELECT * FROM Followers JOIN People
			ON Followers.to_id = People.id
			WHERE Followers.from_id = 2''')
count = 0
print('Connections for id=2:')
for row in cur:
	for row in cur:
		if count < 5: print(row)
		count += 1
	print(count, 'rows.')
cur.close()