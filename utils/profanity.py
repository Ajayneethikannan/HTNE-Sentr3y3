import json, requests

from .secret import API_KEY, API_USER

data = {
  'mode': 'standard',
  'lang': 'en',
  'api_user': API_USER,
  'api_secret': API_KEY
}

def check_profanity(sentence):
    data['text'] = sentence
    response = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)
    output = json.loads(response.text)
    matches = output['profanity']['matches']
    if len(matches) == 0:
      return False
    topics = ', '.join(map(lambda match: match['type'], matches))
    return f'Found {topics} content in the application'

# check_profanity('s3x smoke alcohol n3gro fifth street')
# check_profanity('s3x fifth street')