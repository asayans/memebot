import praw
import requests

'''
    Secrets
'''
CLIENT_ID = 'x'
CLIENT_SECRET = 'x'
PASSWORD = 'x'
USERNAME = 'x'
USERAGENT = 'Dank Memes Collector v0.1 (by /u/niggafiend)'

'''
    OAuth
'''
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     password=PASSWORD, user_agent=USERAGENT,
                     username=USERNAME)

'''
    Functions
'''
# Get top posts of the day for given sub
def get_memes(sub, limit=5):
    spicy_memes = reddit.subreddit(sub).top('day', limit=limit)

    for meme in spicy_memes:
        title = str(meme.title)
        file_name = meme.id
        pic_url = meme.url

        with open('memes_folder\\' + file_name + '.jpg', 'wb') as handle:
            response = requests.get(pic_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

'''
    Get dem spicy memez
'''
subs = ['example_sub'[, 'as many subs as you want here']]

for sub in subs:
    get_memes(sub)
