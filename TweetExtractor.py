#!/usr/bin/env python
##################################################
##				TweetExtractor					##
#Execution of the process
#python TweetExtractor ConfigurationFile.json


from StreamHandler import StreamHandler
import time, tweepy, sys, json, array


def printConfiguration(confData):
	print("The configuration used for the TweetExtractor will be:")
	print("\t API Key:\t\t"+confData["API Key"])
	print("\t API Secret:\t\t"+confData["API Secret"])
	print("\t Access Token:\t\t"+confData["Access Token"])
	print("\t Access Token Secret:\t"+confData["Access Token Secret"])
	print("\t Output File:\t\t"+confData["Output File"])
	print("\t Output Folder:\t\t"+confData["Output Folder"])
	for filter in list(confData["Filter"]):
		print("\t Filter:\t\t"+filter)
	print("\t Tweets per file:\t"+str(confData["Tweets per file"]))


def configure(file):
	try:
		confFile=open(file)		
		confData=json.load(confFile)
		printConfiguration(confData)
		return confData
	except Exception as e:
		print("Error using <<"+file+">> file, check file format, structure and location")
		pass


def createAuth(confData):
	aKey=confData["API Key"]
	aSecret=confData["API Secret"]
	aToken=confData["Access Token"]
	aTokenSecret=confData["Access Token Secret"]
	
	auth = tweepy.OAuthHandler(aKey,aSecret)
	auth.set_access_token(aToken,aTokenSecret)

	return auth


def main():
	file = sys.argv[1]
	confData=configure(file)
	filter=confData["Filter"]
	
	twitterAuth= createAuth(confData)
	twitterListener=StreamHandler(confData)

	twitterStream=tweepy.Stream(auth=twitterAuth,listener=twitterListener)
	
	
	
	twitterStream.filter(track=filter)
	
	
	

if __name__ == '__main__':
    main()