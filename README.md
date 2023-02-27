# Reddit Comment Bot 🤖
#### *it's an automated Reddit comment bot that draws its answers from the GPT-3 API*
  - Pick a subreddit to scan
  - Set your bot's reply with keywords
  - Set the response of GPT–3 and define the invitation to go to *Starton*.
 
## 📋・Requirements
  - [Python](https://www.python.org/downloads/)
  - [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
  - [A Reddit Account](https://www.reddit.com/register/)
## 🚀・Setup
Clone the repository to your local machine:
```sh-session
git clone https://github.com/snyzeroff/Redditbot.git
```
```sh-session
> Add your information in the .env file
> Pick a subreddit to scan
> Set your bot's reply with keywords in the file seleted_keywords.txt
> Define the response of GPT–3 and set the invitation to go to *Starton*.
> run main.py
```


### Reddit App :
1. [Navigate to the Apps page ](https://www.reddit.com/dev/api)
2. Click *create an app*
3. **name:** Set a name for your app
4. **type:** Script
5. **description:** Optional
6. **about url:** Optional
7. **redirect uri:** http://localhost:8080
8. Note the outputted *client id* and *secret*

#### main.py
- Set the subreddit to search (default = "r/web3"):
```python
r.subreddit('web3')
```
- Set the response of GPT–3 + set invitation to go to the *Starton* (in hypertext) website and adds 2 other decoys
``` python
reply_text = response.choices[0].text.format("[starton.io](https://starton.io/)")
reply_text += " Je t'invite à essayer un des templates de [Starton]({}).".format("[starton.io](https://starton.io/)")
comment.reply(reply_text)
```
- Prints that he has found a message to which he has replied
and waits 10 seconds
``` python
print("Réponse envoyée pour le commentaire {}.".format(comment.id))
time.sleep(10)
```
#### .env :
1. **username:** your Reddit username
2. **password:** your Reddit password
3. **client_id:** the outputted client id
4. **client_secret:** the outputted secret
5. **OPENAI_API_KEY:** your OpenAI API key

#### Selected_keywords.txt :
- add the keywords you want in the selected_keywords.txt file so that the bot only responds to comments containing these keywords (*default keywords* : "how to deploy smartcontract?"
; "listen to activity on the blockchain")
```txt
"how to deploy smartcontract?"
"listen to activity on the blockchain"
```
## 📝・Description 

- [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
- [A Reddit API Documentation](https://www.reddit.com/dev/api)

The script is designed to automate the process of replying to Reddit comments for which there are specific keywords on the topic of Web 3.0, using the OpenAI API to generate a reply that is published as a response to the original comment. The script also takes steps to avoid duplicate responses and API request saturation.

The script stores the IDs of comments it has already responded to in a list called "comments_replied_to". This is done to avoid replying to the same comment multiple times.

The comment identifiers are also written to a text file called "comments_replied_to.txt" to save the list between runs of the script.

Finally, the script waits 10 seconds between each iteration of the loop to avoid overloading the Reddit API with requests.

In your command prompt or terminal, navigate to the project directory.

Run the bot.py script by typing python bot.py.

The script will continuously check for new comments in the specified subreddit, and if a comment containing any of the selected keywords is found, the bot will generate a response using the OpenAI API and post it as a reply to the comment.

To stop the script, press CTRL + C in your command prompt or terminal.

### Notes

To avoid replying to the same comment multiple times, the script stores the IDs of the comments it has already replied to in a text file called comments_replied_to.txt in the data directory. If you want to reset the list, simply delete the file.

The script waits for 10 seconds between each loop iteration to prevent the bot from overwhelming the Reddit API with requests.

#### *Fabien, Jérome (or the Starton team) if you have any questions do not hesitate to contact me*

## 💭・ChangeLog

```diff
v0.0.3 ⋮ 27-02-2023
+ Updated the Readme 
+ Added the ChangLog

v0.0.2 ⋮ 26-02-2023
+ Updated the Readme
+ Updated the Main.py file
+ Added the comments_replied_to.txt file
+ Cleaner code

v0.0.1 ⋮ 25-02-2023
+ Added Main Script
+ Cleaned up Code
```

# Author
# [Hi, I'm Paul-Emile Heim! 👋](https://github.com/snyzeroff)

[<img src="https://i.imgur.com/OL5xQWZ.png" width="317" height="317">](https://discord.com/users/1074612809326936094)
## 🔗・Links
[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/snyzeroff)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/paul-ehm-3bb478266/)
[![discord](https://img.shields.io/badge/Discord-4169E1?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/691571567863398430)


-----
[![starton](https://i.imgur.com/c4O6h1Q.png)](https://www.starton.io/)
