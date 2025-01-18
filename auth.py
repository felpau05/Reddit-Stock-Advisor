import requests 

# This function authenticates with Reddit's API and returns the authorization token.
def get_reddit_tokens():

    # Reads API keys from a text file ('reddit_api.txt'). 
    # Ensure you have your own Reddit API keys saved in the file in the following format:
    # CLIENT_ID=<your_client_id>
    # SECRET_KEY=<your_secret_key>
    # password=<your_password>
    
    with open('reddit_api.txt', 'r') as f:
        keys = {line.split('=', 1)[0].strip(): line.split('=', 1)[1].strip() for line in f}

    CLIENT_ID = keys["CLIENT_ID"]
    SECRET_KEY = keys["SECRET_KEY"]

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {'grant_type': 'password', 'username': 'diddyparty9370', 'password': keys["password"]}
    headers = {'User-Agent': 'RSS_API/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'

    return headers
  
