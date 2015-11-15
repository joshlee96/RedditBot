import time
import praw
import pdb
import re
import os
from bot_info import *

while(True):
    # Checks if the bot's username and password exists
    if not os.path.isfile("bot_info.py"):
        print("You must create an info file your username and password")
        exit(1)

    # Bot Name
    user_agent = ("Advisor Bot 0.1")

    # Assigns the user agent and attempts to log in
    r = praw.Reddit(user_agent = user_agent)
    r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

    # If there does not exist a replied posts file (to see where the bot has posted)
    if not os.path.isfile("replied_posts.txt"):
        replied_posts = []

    # If there does exist:
    else:
        with open("replied_posts.txt", "r") as f:
            # Reads and filters the replied threads, and filters out the empty posts
            replied_posts = f.read()
            replied_posts = replied_posts("\n")
            replied_posts = filter(None, replied_posts)


    # Accesses the specific subreddit
    subreddit = r.get_subreddit("pythonforengineers")

    # Checks the "hot" submissions
    for submission in subreddit.get_hot(limit = 15):
        # If the post has NOT been commented on by the bot
        if submission.id not in replied_posts:
            if re.search("beats per minute", submission.title.lower(), re.IGNORECASE):
                submission.add_comment("HAHAHAHAA")
                print("Bot is replying to :", submission.title)
                replied_posts.append(submission.id)
                time.sleep(600)


    with open("replied_posts.txt", "w") as f:
        for post_id in replied_posts:
            f.write(post_id + "\n")
