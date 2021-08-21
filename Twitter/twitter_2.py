import requests, json
import hidden
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

secrets = hidden.oauth()
bearer_token = secrets["bearer_token"]

# Tweet fields are adjustable.
# Options include:
# attachments, author_id, context_annotations,
# conversation_id, created_at, entities, geo, id,
# in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
# possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
# source, text, and withheld
params = {"tweet.fields": "created_at,text,source"}

def create_url(username = "drchuck"):
	# get user ID
	url = "https://api.twitter.com/2/users/by/username/"+username
	request_user_data_by_username = requests.request("GET", url, auth=bearer_oauth)
	# if user ID is known - Replace with user ID below
	user_id = request_user_data_by_username.json()["data"]["id"]
	return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

def bearer_oauth(r):
    # Method required by bearer token authentication.

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r



while True:
	print('')
	acct = input('Enter Twitter Account:')
	if (len(acct) < 1): break
	url = create_url(acct)
	print('Retrieving', url)
	response = requests.request("GET", url, auth=bearer_oauth, params=params)
	json_response = response.json()
	print(json.dumps(json_response, indent=4, sort_keys=True))
	# get the remaining api call count 
	headers = dict(response.headers)
	print('Remaining', headers['x-rate-limit-remaining'])