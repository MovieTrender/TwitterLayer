## Read [Project Documentation](https://github.com/MovieTrender/Documentation "Project Documentation")

##Twitter Layer

This is the first layer of [MovieTrender](https://github.com/MovieTrender "MovieTrender").

Downloads tweets from Twitter and store them in the local folder structure.

Stores tweets in two ways:
- Single tweets. Files with tweet_id as name, and the text of the tweet in the         content.
- Common tweets. CSV files grouping tweets, includes in the file tweet_id, user_id,     followers of the user...

Single tweets will be used for calculating the sentiment, common tweets will be used to break down the information downloaded.


The process was created using [Python](https://www.python.org/ "Python") and [Tweepy](https://github.com/tweepy/tweepy "Tweepy").

More info about Twitter api in [Twitter](https://dev.twitter.com "Twitter")

###Use
Execution

	python TweetExtractor.py Configuration/Configuration.json

###Configuration
The configuration file is a json file with all the parameters needed for the execution of the process:

Parameters in configuration file:
- API Key: Key generated in Twitter account.
- API Secret: Secret key generated in Twitter account.
- Access Token: Access token generated in Twitter account.
- Access Token Secret: Secret token generated in Twitter account.
- Output File: Prefix for the name of the file with tweets downloaded.
- Output Common Folder: Folder where will be stored all the files grouping tweets.
- Output Single Folder: Folder where will be stored the single tweet files (file per   tweet)
- Filter: Filter to be used in the tweets. Only will be downloaded tweets containing   the word specified in the filter.
- Tweets per file: Number of tweets per Common file/ Number of tweet files grouped in   a folder. 


  {
  
      "API Key": "",
      
      "API Secret":"",
      
      "Access Token":"",
      
      "Access Token Secret":"",
      
      "Output File": "Tweets",
      
      "Output Common Folder":"Data",
      
      "Output Single Folder":"Classify",
      
      "Filter": ["Filter1","Filter2"],
      
      "Tweets per file":50000
  
  }


###Local Folder Structure

The local folder structure used by the process is the following:

/Root/Configuration:
	Folder with configuration files.

/Root/Data;
	Folder with common tweet files.

/Root/Classify:
	Folder with single tweet files.

Once that one file or folder (files for common tweet files, folder for single tweets( is ready to be processed in the next step the flag ACK is added to the name.
















