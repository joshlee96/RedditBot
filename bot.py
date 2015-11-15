import time
import praw
import os
from bot_info import *
from input import *


# Open all the text files, distribute data into 3 arrays for each faculty
sci_names, sci_programs, sci_emails = makearray("science.txt")
arts_names, arts_programs, arts_emails = makearray("arts.txt")
math_names, math_programs, math_emails = makearray("math.txt")
eng_names, eng_programs, eng_emails = makearray("engineering.txt")
ahs_names, ahs_programs, ahs_emails = makearray("ahs.txt")
env_names, env_programs, env_emails = makearray("env.txt")



# Checks if the bot's username and password exists
if not os.path.isfile("bot_info.py"):
    print("You must create an info file for your username and password")
    exit(1)

# Bot Name
user_agent = ("Advisor Bot 1.0")

# Assigns the user agent and attempts to log in
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
subreddit = r.get_subreddit('uwaterloo')

while True:
    subreddit_comments = subreddit.get_comments()  #Allows for accesing what is in the Reddit comments

    # If there does not exist a replied posts file (to see where the bot has posted)
    # Create array to hold the files
    if not os.path.isfile("replied_posts.txt"):
        replied_posts = []

    # If it does exist, read the old file, then add all the posts in the txt to the array.
    else:
        with open("replied_posts.txt", "r") as f:
            # Reads and filters the replied threads, and filters out the empty posts
            replied_posts = f.read()
            replied_posts = replied_posts.splitlines()

    flattened_comments = praw.helpers.flatten_tree(subreddit_comments)
    # Checks the new comments
    for comment in flattened_comments:

        """ If the post has NOT been commented on by the bot,
        Reads the comment made by a user and returns the appropriate list of advisors
         Or if the keyword is incorrectly used, replies with a comment providing instructions on proper usage"""
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
            elif "!advisor" in comment.body.lower() and "!advisor <faculty>" not in comment.body.lower():
                comment.reply("Please enter command in the form: !advisor <faculty> (Without brackets)\n\n"
                              "Faculty keywords: arts, math, engineering, science, ahs, environment\n\n"
                              "Bot was created at EngHack Fall 2015")
                print("Bot is posting help to: ", comment.body)
                replied_posts.append(comment.id)
            with open("replied_posts.txt", "w") as f:
                for comment_id in replied_posts:  #Writes the comment IDs so replies aren't repeated for comments
                    f.write(comment_id + "\n")

    time.sleep(10)  #delay timer for program