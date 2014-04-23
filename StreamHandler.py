from tweepy import StreamListener
import json, time, sys, csv

class StreamHandler(StreamListener):

    def __init__(self, confData):
        self.counter = 0
        self.outputFile= confData["Output File"]
        self.outputFolder= confData["Output Folder"]
        self.chunkSize=confData["Tweets per file"]
        self.output  = csv.writer(open(self.outputFolder+'//'+self.outputFile+'-'+time.strftime('%Y%m%d-%H%M%S')+'.csv', 'wb+'))

        
        self.output.writerow(["user_id","user_name","user_followers_count","user_friends_count","user_timezone","coordinates","created_at","tweet"])
        

    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return false




    def on_status(self, status):
    
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

        if self.counter >= self.chunkSize:
            self.output.close()
            self.output = open(self.outputFolder+'//'+self.outputFile+'-'+time.strftime('%Y%m%d-%H%M%S')+'.json', 'w')
            self.counter = 0

        return


    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 