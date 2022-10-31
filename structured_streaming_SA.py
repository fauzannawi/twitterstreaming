from pyspark.sql import SparkSession
from textblob import TextBlob
import time
import matplotlib.pyplot as plt
start_time = time.time()

def main():
    #create spark session
    spark = SparkSession.builder.getOrCreate()
    stream(spark, 60) #stop after 60s

def stream(session, duration):    
    #subscribe to kafka stream
    kstream = session \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "kafkatrial") \
        .load()
    #select tweets column as cast as string. Kafka streams values in binary,so need to convert
    tweets = kstream.selectExpr("CAST(value AS STRING)")
    # Have all the aggregates in an in-memory table.
    tweets \
        .writeStream \
        .queryName("aggregates") \
        .outputMode("append") \
        .format("memory") \
        .start() \
        .awaitTermination(duration)
  
    #query the in-memory table and convert to RDD
    df_RDD = session.sql("select * from aggregates").rdd
    #RDD transformation
    tweettextpolarity = df_RDD.map(lambda x:x.value.split(',')) \
        .map(lambda x:x[0])\
        .map(lambda x:TextBlob(x).sentiment.polarity)
    pos = tweettextpolarity.filter(lambda x:x > 0.0).count()
    neg = tweettextpolarity.filter(lambda x:x < 0.0).count()
    print('pos: ',pos)
    print('neg: ',neg)
    print("Processing time:","--- %s seconds ---" % (time.time() - start_time))
    make_plot(pos,neg)

def sentiment(text):
    if text > 0:
        return 'Positive'
    elif text < 0:
        return 'Negative'

def make_plot(pos,neg):
    plt.pie([pos,neg])
    plt.legend(['positive sentiment','negative sentiment'], loc = 'best', fontsize = 10)
    plt.show()

if __name__=="__main__":
    main()
#spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0  structured_streaming_SA.py
