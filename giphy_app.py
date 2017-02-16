import requests
import random
import json

url = 'http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC'
r = requests.get(url)
jr = r.json()

def randNum():
    return random.randrange(1,25)

def randGiph():
    return jr['data'][randNum()]['embed_url']
    
