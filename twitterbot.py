import tweepy
import config
import redditnews
import text2emoji

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#tweet clean up
user = api.me()
tweetHistory = api.user_timeline(id = user.id)
for tweet in tweetHistory:
    api.destroy_status(id = tweet.id)

headlines = redditnews.getRedditHeadlines()
for headline in headlines:
    api.update_status(status = text2emoji.sentence_to_emoji(headline))

print('End')
