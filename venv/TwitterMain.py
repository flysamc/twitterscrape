import tweepy
from tweepy import OAuthHandler

consumer_key = 'QEBCYVQZCyqE3H3WteTs7BNP9'
consumer_secret = 'bd4GdAs8fVqAKtNkyRILQ4DIV7NWdXH5MxwB7Zzeyq9JSFbqJJ'
access_token = '1059703438559240192-Qk4m9A9VCxVGwjwulXPLkDZOaXuZTQ'
access_secret = 'zRO4v6lcyNI8AlrrPiQ4Z7MJ7OP4ID6d9Dqmwa82XOxJc'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)