#!/usr/bin/env python
"""TweetExtractor.py

Main module for downloading tweets from Twitter using tweepy
	
Example:
	$TweetExtractor.py Configuration/ConfigurationFile.json

"""

from StreamHandler import StreamHandler
import time, tweepy, sys, json, array


def printConfiguration(confData):
	"""
	Print all the configuration read from the configuration file
	
	Args:
		confData(json): Json object with all the configuration values
	
	"""
	print("The configuration used for the TweetExtractor will be:")
	print("\t API Key:\t\t"+confData["API Key"])
	print("\t API Secret:\t\t"+confData["API Secret"])
	print("\t Access Token:\t\t"+confData["Access Token"])
	print("\t Access Token Secret:\t"+confData["Access Token Secret"])
	print("\t Output File:\t\t"+confData["Output File"])
	print("\t Output Common Folder:\t\t"+confData["Output Common Folder"])
	print("\t Output Single Folder:\t\t"+confData["Output Single Folder"])
	#The filter is a list of keywords, at least one must be in the tweet
	for filter in list(confData["Filter"]):
		print("\t Filter:\t\t"+filter)
	print("\t Tweets per file:\t"+str(confData["Tweets per file"]))





def configure(file):
	"""	
	Open the configuration file and load it into a json object.
	The file must exist and the format must be a json file.
	
	Args:
		file(str): Path to the json file with the configuration information.
	
	Returns:
		Json: Json object with all the configuration information.
		
	"""
	try:
		confFile=open(file)		
		confData=json.load(confFile)
		printConfiguration(confData)
		return confData
	#If the file is not in the expect format, or is not found an exception is raised
	except Exception as e:
		print("Error using <<"+file+">> file, check file format, structure and location")
		pass




def createAuth(confData):
	"""
	Create the Authentication for using Twitter API
	
	Args:
		confData(json): Json object with all the configuration information.
	
	Returns:
		OAuthHandler: Authenticatin handler used for connecting in Twitter API

	"""
	aKey=confData["API Key"]
	aSecret=confData["API Secret"]
	aToken=confData["Access Token"]
	aTokenSecret=confData["Access Token Secret"]
	
	auth = tweepy.OAuthHandler(aKey,aSecret)
	auth.set_access_token(aToken,aTokenSecret)

	return auth





def main():
	"""
	Main module of the TweetExtractor process.
	Take the first argument (which is the path to the configuration file),
	load the configuration information stored on it and connect to Twitter.
	Downloads from Twitter all the sample tweets matching with the query.

	"""
	#Only will work if the first argument is specified, in other case will show
	#usage of the process and will finish.
	try:
		file = sys.argv[1]
		confData=configure(file)
		filter=confData["Filter"]

		twitterAuth= createAuth(confData)
		twitterListener=StreamHandler(confData)
		twitterStream=tweepy.Stream(auth=twitterAuth,listener=twitterListener)

		#Filtering by the filters defined in the configuration and
		#language= English
		twitterStream.filter(track=filter, languages=["en"])
	
	except IndexError:
		print "Use of TweetExtractor:"
		print "\t TwwetExtractor.py configurationFile.json"	
	except KeyboardInterrupt:
		exit(0)
	

if __name__ == '__main__':
	main()