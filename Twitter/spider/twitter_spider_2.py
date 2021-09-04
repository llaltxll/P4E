# import the functions to get user friends list by user name from the 2.0 API
import twitter_user_followers_by_username as tuser
from friends_list_response import js_dummy
import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
			(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Followers
			(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

while True:
	acct = input('Enter a twitter account, or quit: ')
	if (acct == 'quit'): break
	if (len(acct) < 1):
		# use unretrieved account from DB
		cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
		try:
			(id, acct) = cur.fetchone()
		except:
			print('No unretrieved Twitter acounts found')
			continue
	else:
		# check if account exists, use existing account id, if not create new entry
		cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
					(acct, ))
		try:
			id = cur.fetchone()[0]
		except:
			cur.execute('''INSERT OR IGNORE INTO People
						(name, retrieved) VALUES (?, 0)''', (acct, ))
			conn.commit()
			if cur.rowcount != 1:
				print('Error inserting account:', acct)
				continue
			id = cur.lastrowid

	# This is modified to use the functions written in asaeparate file for 2.0 copatability
	# js dummy for testing
	# js = js_dummy
	print("retrieving ", acct, "...")
	# 2do we should probably keep the twitter user_ID in our DB as-well...
	user_id = tuser.get_userID(acct)
	url = tuser.create_url(user_id)
	# in params we ask for the pinned tweet for eavh user and limit the results to 100 users
	params = {"user.fields": "pinned_tweet_id",
		"max_results": 100}
	js = tuser.connect_to_endpoint(url, params)
	# print(json.dumps(js, indent=4, sort_keys=True))

	cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))
	# in case the current account has no friends marks account as retrieved in db an continue
	if 'data' not in js:
		continue

	countnew = 0
	countold = 0

	for u in js['data']:
		friend = u['username']
		print(friend)
		cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
					(friend, ))
		try:
			friend_id = cur.fetchone()[0]
			countold += 1
		except:
			cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
				VALUES (?, 0)''', (friend, ))
			conn.commit()
			if cur.rowcount != 1:
				print('Error inserting account:', friend)
				continue
			friend_id = cur.lastrowid
			countnew += 1
		cur.execute('''INSERT OR IGNORE INTO Followers (from_id, to_id)
					VALUES (?, ?)''', (id, friend_id))
	print('New acounts=', countnew, ' revisited=', countold)
	conn.commit()

cur.close()