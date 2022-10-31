# twitterstreaming
## background
During my Data Engineering training, the instructor showed an example of Spark Streaming using Twitter API.
The streaming was done via kafka, and the sentiment of the tweets was analysed using the TextBlob library.

I tried to run the code upon receipt of the API key from Twitter, but the API replied with error 403. My API key is only for API V2, while the code from the training is based on API v1.1. Hence, the 403. The tweepy library started supporting Twitter API v2 since version 4.0. I tried to upgrade the tweepy, as well as the other packages in the training VM (running Centos 7) but no cigar. The VM was unsurprisingly sluggish, mainly due to my laptop's limitations. Hence, I decided to prepare the environment in Windows and try to make the Twitter streaming works.

## environment
Below are the versions running on my pc

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

## running the script
1. Setup Kafka zookeeper, kafka server, producer and receiver.
2. Run structured_streaming_twitter.py in pyspark. Be sure that the API key is entered in the script. Default keyword for tweets streaming is "bitcoin".

`spark-submit structured_streaming_twitter.py`

3.Run structured_streaming_SA.py

`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0  structured_streaming_SA.py`

## to-do
1. Processing using foreach method instead of writing to the table and covert to RDD. I managed to do the sentiment analysis using foreach, however, unable to sums all the results from each epoch. Need to learn more about object serialization and deserialization.
