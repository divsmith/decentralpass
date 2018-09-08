from pprint import pprint

import praw
from config import CLIENT_ID, CLIENT_SECRET, REDDIT_PASSWORD, REDDIT_USERNAME, REDDIT_USERAGENT


COMMENT_LIMIT_PER_POST = 100


def main():
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         password=REDDIT_PASSWORD, username=REDDIT_USERNAME,
                         user_agent=REDDIT_USERAGENT)
    top_posts = reddit.subreddit("bitcoin").top(time_filter="month")
    for post in top_posts:
        pprint(post.title)
        post_comments = post.comments
        post_comments.replace_more(limit=COMMENT_LIMIT_PER_POST)
        for comment in post_comments.list():
            pprint(comment.body)


if __name__ == "__main__":
    main()