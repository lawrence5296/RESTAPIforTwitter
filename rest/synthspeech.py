import requests
import pprint
import datetime
import argparse
import subprocess
import json
import time
import os
import sys


def main():
	### Set environment
	tmp = "./data"
 	key = "Please input key"
	
	### Chose target url
	url = "https://api.apigw.smt.docomo.ne.jp/aiTalk/v1/textToSpeech?APIKEY="+key
	print url

	### Set params
	prm = {
			"speaker":"nozomi",
			"pitch":"1",
			"range":"1",
			"rate":"1",
			"volume":"1.5"
			}

	### Set argument
	parser = argparse.ArgumentParser()
	parser.add_argument("--text",type=str,required=True)
	args = parser.parse_args()
	text = args.text

	### Create SSML
	xml = u'<?xml version="1.0" encoding="utf-8" ?>'
	speakerv = '<speak version="1.1">'
	prosody = '<prosody rate="'+ prm['rate'] +'" pitch="' + prm['pitch'] +'" range="'+ prm['range'] +'">'
	voice = '<voice name="' + prm["speaker"] + '">'
	xml += speakerv + voice + prosody + text + '</prosody></voice></speak>'
	xml = xml.encode("UTF-8")
	# print xml

	### Requests"
	response = requests.post(
		url,
		data=xml,
		headers={
				'Content-Type' : 'application/ssml+xml',
				'Accept' : 'audio/L16',
				'Content-Length' : len(xml)
		}
	)

	if response.status_code != 200 :
			print("Error API : %s" % response.status_code)
			exit()
	else : 
			print "Success"
					
	rawFile = "speech.raw"
	#wavFile = "sppech.wav"
	
	fp = open(tmp + rawFile, 'wb')
	fp.write(response.content)
	fp.close()
	
	print("Save Binary Data : " + tmp + rawFile)
		
		
	#print r.encoding
	#print r.headers
	#print r.status_code
	#print json.dumps(r.json(), indent=4)



if __name__ == "__main__":
	main()	
