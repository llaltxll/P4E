# import the functions to get user friends list by user name from the 2.0 API
import twitter_user_followers_by_username as tuser
from friends_list_response import js_dummy
import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
			CREATE TABLE IF NOT EXISTS Twitter
			(name TEXT, retrieved INTEGER, friends INTEGER)''')

while True:
	acct = input('Enter a twitter account, or quit: ')
	if (acct == 'quit'): break
	if (len(acct) < 1):
		cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
		try:
			acct = cur.fetchone()[0]
			print(acct)
		except:
			print('No unretrieved Twitter acounts found')
			continue

	# This is modified to use the functions written in asaeparate file for 2.0 copatability
	# js dummy for testing
	# js = js_dummy
	user_id = tuser.get_userID(acct)
	url = tuser.create_url(user_id)
	# in params we ask for the pinned tweet for eavh user and limit the results to 20 users
	params = {"user.fields": "pinned_tweet_id",
		"max_results": 20}
	js = tuser.connect_to_endpoint(url, params)
	# print(json.dumps(js, indent=4, sort_keys=True))

	cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

	countnew = 0
	countold = 0

	# in case the current account has no friends marks account as retrieved in db an continue
	if 'data' not in js:
		cur.execute('UPDATE Twitter SET retrieved = 1 WHERE name = ?', (acct, ))
		continue

	for u in js['data']:
		friend = u['username']
		print(friend)
		cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
		try:
			count = cur.fetchone()[0]
			cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
			countold += 1
		except:
			cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
				VALUES (?, 0, 1)''', (friend, ))
			countnew += 1
	print('New acounts=', countnew, ' revisited=', countold)
	conn.commit()

cur.close()