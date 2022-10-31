import tweepy
from kafka import KafkaProducer

#define streaming client   
class IDPrinter(tweepy.StreamingClient):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)
        self.producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

    def on_tweet(self, tweet):
        msg = tweet.text.encode("ascii", "ignore")
       
        try:
            self.producer.send("kafkatopic", msg)            
        except Exception as e:
            print(e)
            return False
        return True
        
if __name__ == '__main__':

    bearer_token = 'bearer_token'
    printer = IDPrinter(bearer_token)

    #delete existing rules
    rules = printer.get_rules().data
    print('Displaying existing rules')
    print(rules)
    if rules:
        rules_id = [z[-1] for z in rules]
        print('Deleting existing rules')
        printer.delete_rules(rules_id)
    else:
        print('No existing rule')

    rules1 =str(printer.get_rules().data)
    if rules1 == 'None':
        print('All rules deleted')

    #stream keyword
    keyword = "bitcoin"
    printer.add_rules(tweepy.StreamRule(keyword))
    print('Streaming tweets. Keyword:', keyword)
    printer.filter()