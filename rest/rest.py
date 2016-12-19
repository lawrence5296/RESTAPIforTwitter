import requests
import json
import time
from requests_oauthlib import OAuth1Session


def main():
	### Set environment
	CK = "Please input CK"
	CS = "Please input CS"
	AT = "Please input AT"
	AS = "Please input AS"

	### Set start time
	start = time.clock()
	
	### Chose target url
	#url = "http://search.twitter.com/search.json"
	#url = "https://api.twitter.com/1.1/trends/place.json"
	url = "https://api.twitter.com/1.1/statuses/update.json"

	### Set tweet
	payload = {"status": "This tweet is a test of RESTAPI from python scripts."}

	### Set Oauth
	twitter = OAuth1Session(CK,CS,AT,AS)

	### Requests REST API
	r = twitter.post(url,params=payload)
	
	### Results
	if r.status_code == 200:
		print "Success requests"
	else:
		print "Error: %d" % r.status_code
	#print r.text
	#print r.encoding
	#print r.headers
	#print r.status_code
	#print json.dumps(r.json(), indent=4)

	### Set finish time and print
	executetime = time.clock() - start
	print "time = %f" %(executetime)


if __name__ == "__main__":
	main()	
