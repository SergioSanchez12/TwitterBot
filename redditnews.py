import praw
import config

def getRedditHeadlines():
    reddit = praw.Reddit(client_id=config.CLIENT_ID,
                         client_secret=config.CLIENT_SECRET,
                         user_agent="/u/EmojiNews",
                         username=config.USER_NAME,
                         password=config.PASSWORD)

    print(reddit.user.me)

    newsData = reddit.subreddit('worldnews').top('day', limit = 5)
    headline = []
    for submission in newsData:
        headline.append(submission.title)

    return headline

