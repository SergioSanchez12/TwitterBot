print('Hello World')
import tweepy
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
res = api.update_status(status = 'Third tweet by Emoji News')
user = api.me()
tweetHistory = api.user_timeline(id = user.id)

for tweet in tweetHistory:
    api.destroy_status(id = tweet.id)

print('End')
