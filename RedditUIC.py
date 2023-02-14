import praw
import os
from praw.models import MoreComments
from dotenv import load_dotenv

load_dotenv()
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

reddit = praw.Reddit(
    client_id = REDDIT_CLIENT_ID,
    client_secret = REDDIT_CLIENT_SECRET,
    user_agent = REDDIT_USER_AGENT,
)

def scrape(subreddit):

    users1 = []

    for submission1 in subreddit.top(time_filter='week', limit=5):
        users1.append(submission1.author)
        print(submission1.permalink)
        for comment in submission1.comments:
            if isinstance(comment, MoreComments):
                continue
            users1.append(comment.author)

    return users1

firstSub = reddit.subreddit(input('Enter the name of the first subreddit: '))
secondSub = reddit.subreddit(input('Enter the name of the second subreddit: '))

print('subreddit1: ' + firstSub.display_name)
print('subreddit2: ' + secondSub.display_name)

result1 = scrape(firstSub)
result2 = scrape(secondSub)

print('\nList 1\n', result1)
print('\nList 2\n', result2)

common_list = set(result1).intersection(result2)

print('\nUsers in common: ', common_list)
