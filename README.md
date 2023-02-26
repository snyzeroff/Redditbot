# Bot Reddit
#### *it's an automated Reddit comment bot that draws its answers from the GPT-3 API*
  - Pick a subreddit to scan
  - Designate a specific comment to search for
  - Set your bot's reply with keywords


## 📋・Requirements
  - [Python](https://www.python.org/downloads/)
  - [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
  - [A Reddit Account](https://www.reddit.com/register/)
## 🚀・Setup
```sh-session
> Add your information in the .env file
> Set the subreddit to search 
> Enter your keywords in the file seleted_keywords.txt
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
Set the subreddit to search (default = "r/web3"):
```python
r.subreddit('web3')
```
Set the response of GPT – 3 + set invitation to go to the ***Starton*** (in hypertext) website and adds 2 other decoys
``` python
reply_text = response.choices[0].text.format("[starton.io](https://starton.io/)")
reply_text += " Je t'invite à essayer un des templates de [Starton]({}).".format("[starton.io](https://starton.io/)")
comment.reply(reply_text)
```
Prints that he has found a message to which he has replied
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
add the keywords you want in the selected_keywords.txt file so that the bot only responds to comments containing these keywords (*default keywords* : "how to deploy smartcontract?"
; "listen to activity on the blockchain")
```txt
"how to deploy smartcontract?"
"listen to activity on the blockchain"
```
 
 
