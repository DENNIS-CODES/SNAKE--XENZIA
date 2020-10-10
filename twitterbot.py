import tweepy
import time

auth = tweepy.OAuthHandler('TketZYCmYQCpw6mJiivFTg68O','M4Jai4LbOhyTfsVs4Zz6PUAJN9KBnoy4W7JlwgwPLpTKpC16Qv')
auth.set_access_token('3173088059-cFmQSxrzmClQEfD67V0xONWRsMjpWeLEmt4jAqP','MJhRiEU9BtCLCwkn3aDJ1iJZFFEQNiQGlCGiImLKOST9v')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '100DaysOfCode'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

