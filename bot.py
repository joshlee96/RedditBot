import time
import praw
import pdb
import re
import os
from bot_info import *
from input import *


# Open all the text files
sci_names, sci_programs, sci_emails = makearray("science.txt")
arts_names, arts_programs, arts_emails = makearray("arts.txt")
math_names, math_programs, math_emails = makearray("math.txt")
eng_names, eng_programs, eng_emails = makearray("engineering.txt")
ahs_names, ahs_programs, ahs_emails = makearray("ahs.txt")
env_names, env_programs, env_emails = makearray("env.txt")



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
                comment.reply(printgraph(eng_names, eng_programs, eng_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor arts" in comment.body.lower():
                comment.reply(printgraph(arts_names, arts_programs, arts_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor science" in comment.body.lower():
                comment.reply(printgraph(sci_names, sci_programs, sci_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor math" in comment.body.lower():
                comment.reply(printgraph(math_names, math_programs, math_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor ahs" in comment.body.lower():
                comment.reply(printgraph(ahs_names, ahs_programs, ahs_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "!advisor environment" in comment.body.lower():
                comment.reply(printgraph(env_names, env_programs, env_emails))
                print("Bot is replying to :", comment.body)
                replied_posts.append(comment.id)
            elif "doo-do do dooooo" in comment.body.lower():
                comment.reply(printgraph(env_names, env_programs, env_emails))
                replied_posts.append(comment.id)
            with open("replied_posts.txt", "w") as f:
                for comment_id in replied_posts:
                    f.write(comment_id + "\n")



    time.sleep(30)