import requests
import json
import time
import sys
from requests_oauthlib import OAuth1Session


def main():
	### Confirm argv
	argv = sys.argv
	if len(argv) != 2:
			print "Usage: python %s \"tweetmsg\"" % argv[0] 
			quit()

	### Set environment
	CK = "Please input CK"
	CS = "Please input CS" 
	AT = "Please input AT"
	AS = "Please input AS"

	### Set start time
	# start = time.clock()
	
	### Chose target url
	url = "https://api.twitter.com/1.1/statuses/update.json"

	### Set tweet
	print "Post Tweet : %s" % argv[1] 
	payload = {"status": argv[1]}

	### Set Oauth
	twitter = OAuth1Session(CK,CS,AT,AS)

	### Requests REST API
	r = twitter.post(url,params=payload)
	
	### Results
	if r.status_code == 200:
		print "Success Tweet"
	else:
		print "Error: %d" % r.status_code
	#print r.text
	#print r.encoding
	#print r.headers
	#print r.status_code
	#print json.dumps(r.json(), indent=4)

	### Set finish time and print
	# executetime = time.clock() - start
	# print "time = %f" %(executetime)


if __name__ == "__main__":
	main()	
