import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

def get_userID(username):
	# if user ID unknown use fill below
	# username = "drchuck"
	url = "https://api.twitter.com/2/users/by/username/"+username
	request_user_data_by_username = requests.request("GET", url, auth=bearer_oauth)
	user_id = request_user_data_by_username.json()["data"]["id"]
	return user_id

def create_url(user_id):
	return "https://api.twitter.com/2/users/{}/followers".format(user_id)

# def get_params():
# 	# Tweet fields are adjustable.
#     # Options include:
#     # attachments, author_id, context_annotations,
#     # conversation_id, created_at, entities, geo, id,
#     # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
#     # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
#     # source, text, and withheld
#     return {"tweet.fields": "created_at,text,source"}

def bearer_oauth(r):
    # Method required by bearer token authentication.

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params=''):
	response = requests.request("GET", url, auth=bearer_oauth, params=params)
	print(response.status_code)
	# get the remaining api call count 
	headers = dict(response.headers)
	# print('Remaining', headers['x-rate-limit-remaining'])
	if response.status_code != 200:
		raise Exception(
			"Request returned an error: {} {}".format(
				response.status_code, response.text
			)
		)
	return response.json()


def main():
	user_id = get_userID("drchuck")
	url = create_url(user_id)
	# params = get_params()
	json_response = connect_to_endpoint(url)
	print(json.dumps(json_response, indent=4, sort_keys=True))
	# count text length for each tweet
	# for tweets in json_response["data"]:
	# 	print(len(tweets["text"]))

if __name__ == "__main__":
	main()