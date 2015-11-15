import time
import praw
import pdb
import re
import os
from bot_info import *


# Open all the text files
def makearray(file, arrayname):
    with open(file, "r"):
        arrayname = []
        lines = file.readlines()
        arrayname = lines.split("|")



# Checks if the bot's username and password exists
if not os.path.isfile("bot_info.py"):
    print("You must create an info file your username and password")
    exit(1)

# Bot Name
user_agent = ("Advisor Bot 0.1")

# Assigns the user agent and attempts to log in
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
subreddit = r.get_subreddit('pythonforengineers')

while True:
    subreddit_comments = subreddit.get_comments()

    # If there does not exist a replied posts file (to see where the bot has posted)
    if not os.path.isfile("replied_posts.txt"):
        replied_posts = []

    # If there does exist:
    else:
        with open("replied_posts.txt", "r") as f:
            # Reads and filters the replied threads, and filters out the empty posts
            replied_posts = f.read()
            replied_posts = replied_posts.split("\n")

    flat_comments = praw.helpers.flatten_tree(subreddit_comments)
    # Checks the "hot" submissions
    for comment in flat_comments:
        # If the post has NOT been commented on by the bot
        if comment.id not in replied_posts:
            if "!advisor engineering" in comment.body.lower():
                print(comment.body)
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor arts" in comment.body.lower():
                print(comment.body)
            elif "!advisor science" in comment.body.lower():
                print(comment.body)
            elif "!advisor math" in comment.body.lower():
                print(comment.body)
            elif "!advisor ahs" in comment.body.lower():
                print(comment.body)
            elif "!advisor environment" in comment.body.lower():
                print(comment.body)

    with open("replied_posts.txt", "w") as f:
        for post_id in replied_posts:
            f.write(post_id + "\n")

    time.sleep(30)