import requests
import json
import time
from requests_oauthlib import OAuth1Session


def main():
	### Set environment
	CK = "Please input CK"
	CS = "Please input CS" 
	AT = "Please input AT"
	AS = "PLease input AS"

	### Set start time
	start = time.time()
	
	### Chose target url
	url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

	### Set params
	payload = {}

	### Set Oauth
	twitter = OAuth1Session(CK,CS,AT,AS)

	### Requests REST API
	r = twitter.get(url,params=payload)
	
	### Set finish time
	executetime = time.time() - start

	### Results
	if r.status_code == 200:
		print "Success requests"
		#print json.dumps(r.json(),indent=4)
		timeline = json.loads(r.text)
		for tweet in timeline:
				print(tweet["text"])
	else:
		print "Error: %d" % r.status_code
		print r.text
	#print r.text
	#print r.encoding
	#print r.headers
	#print r.status_code
	#print json.dumps(r.json(), indent=4)

	### Set finish time and print
	print "time = %f" %(executetime)


if __name__ == "__main__":
	main()	
