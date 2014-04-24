"""StreamHandler.py

Handler for the Twitter streaming

"""
from tweepy import StreamListener
import json, time, sys, csv

class StreamHandler(StreamListener):
	"""
	StreamHandler for Twitter streaming
	
	"""
	
	def __init__(self, confData):
		"""
		Initialize the local variables
		
		Args:
			confData(json): Json object with all the configuration values
		
		"""
		
		self.counter = 0
		self.outputFile= confData["Output File"]
		self.outputFolder= confData["Output Folder"]
		self.chunkSize=confData["Tweets per file"]
        
		#Create the file (with timestamp) for all the Tweets downloaded. 
		self.output  = csv.writer(open(self.outputFolder+'//'+self.outputFile+'-'+time.strftime('%Y%m%d-%H%M%S')+'.csv', 'wb+'))

		#We dont need headers in the files generated
		self.output.writerow(["user_id","user_name","user_followers_count","user_friends_count","user_timezone","coordinates","created_at","tweet"])
        
        
	def on_data(self, data):
		"""
		When receiving data, split on Warning and Data, rest will be skip.
		Warnings will be shown in command line, data will be written to the csv
		file.
		
		Args:
			data(str): Json received by Twitter Streaming.
		
		"""
        
		if  'in_reply_to_status' in data:
			self.on_status(data)
		elif 'warning' in data:
			warning = json.loads(data)['warnings']
			print warning['message']
			return false




	def on_status(self, status):
		"""
		Handles the tweet received.
		Transforms information received to a JSON object, extract the information
		from the fields and write a new row to the CSV file.
		
		When the number of rows in the CSV is higher than the limit in the configuration,
		closes the file and create a new one with the timestamp.
	
		Args:
			status(str): Tweet received by Twitter Streaming.
	
		"""
    
		tweet = json.loads(status)
    	
		user_id=tweet["user"]['id']
		user_name=tweet["user"]['name'].encode('UTF-8')
		user_followers=tweet["user"]['followers_count']
		user_friends=tweet["user"]['friends_count']
		user_timezone=tweet["user"]['time_zone']
		coordinates=tweet["coordinates"]
		created_at=tweet["created_at"]
		tweet=tweet["text"].encode('UTF-8')
		
		self.output.writerow([user_id,user_name,user_followers,user_friends,user_timezone,coordinates,created_at,tweet])
    	
    	  
		self.counter += 1

		#If the limit for the file is reached, the file is closed and a new one is opened.
		if self.counter >= self.chunkSize:
			self.output.close()
			self.output = open(self.outputFolder+'//'+self.outputFile+'-'+time.strftime('%Y%m%d-%H%M%S')+'.json', 'w')
			self.counter = 0

		return

	def on_error(self, status_code):
		"""
		On error, the error is shown in the command line
	
		"""
		sys.stderr.write('Error: ' + str(status_code) + "\n")
		return False
        
        

	def on_timeout(self):
		"""
		On timeout sleeps for 60 seconds and try again.
	
		"""
		sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
		time.sleep(60)
		return 