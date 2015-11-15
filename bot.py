import praw

user_agent = ("Advisor Bot")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("uwaterloo")

for submission in subreddit.get_new(limit = 5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("----------------------------------------------------\n")

