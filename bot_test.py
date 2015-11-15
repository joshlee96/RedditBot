import praw
import time
import praw
import pdb
import re
import os

r = praw.Reddit('Comment parser')

subreddit = r.get_subreddit('uwaterloo')

while(True):
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
            #replied_posts = filter(None, replied_posts)


    #for submission in subreddit.get_hot(limit = 15):
    flat_comments = praw.helpers.flatten_tree(subreddit_comments)
    for comment in flat_comments:

        if '' in comment.body.lower() and comment.id not in replied_posts:
            print(comment.body)
            replied_posts.append(comment.id)


    with open("replied_posts.txt", "w") as f:
        for post_id in replied_posts:
            f.write(post_id + "\n")


    time.sleep(30)
# flat_comments = praw.helpers.flatten_tree(subreddit_comments)
# print(flat_comments.body)

