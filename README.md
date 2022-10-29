# twitterstreaming
## background
During my Data Engineering training, the instructor showed an example of Spark Streaming using Twitter API.
The streaming was done via kafka and the sentiment of the tweets were analyzed using TextBlob library
I received the API key from Twitter and tried to run the code, but the API replied with error 403. I believe my API key is only for API V2, while the code from the training is based on API v1.1. The tweepy library started supporting twitter API v2 since version 4.0. I tried to upgrade the tweepy at the training VM (running Centos 7) but no cigar. Then, I decided to prepare the environment in Windows and try to make the twitter streaming works.

##environment
Below are the versions running in  my pc

Windows
- conda 22.9.0
- python 3.9.12
- tweepy 4.10.1
- kafka_2.13-3.2.3
- kafka-python 2.02
- spark3.3.0
- hadoop3.3.4

As a comparison, below are the versions running in the VM 

VM
- conda 4.2.9
- python 3.5.2
- tweepy 3.5.0
- kafka_2.10 0.9.0
- kafka-python 1.35
- spark1.6.0
- hadoop2.6.0
