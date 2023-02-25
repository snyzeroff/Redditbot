import praw
import os
import time
import openai
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PASSWORD'),
                     user_agent=('user_agent'))

subreddit = reddit.subreddit('r/web3')

openai.api_key = os.getenv('OPENAI_API_KEY')

with open('keywords/selected_keywords.txt', 'r') as f:
    selected_keywords = [line.strip() for line in f]

for comment in subreddit.stream.comments(skip_existing=True):
    if any(keyword in comment.body for keyword in selected_keywords):
        print("Comment trouvé avec les mots clés suivants : {}".format(selected_keywords))
        response = openai.Completion.create(engine="text-davinci-002",
                                            prompt=comment.body,
                                            max_tokens=150)
        reply_text = response.choices[0].text.format("[starton.io](https://starton.io/)")
        reply_text += " Je t'invite à essayer un des templates de [Starton]({}).".format("[starton.io](https://starton.io/)")
        comment.reply(reply_text)
        print("Réponse envoyée pour le commentaire {}.".format(comment.id))
        time.sleep(10)