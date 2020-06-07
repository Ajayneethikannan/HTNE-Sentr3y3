import json, requests

# from .secret import API_KEY, API_USER

data = {
  'mode': 'standard',
  'lang': 'en',
  'api_user': '48799953',
  'api_secret': 'Z8MiBiTV86X9j2sAXn2F'
}

def check_profanity(sentence):
    data['text'] = sentence
    response = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)
    output = json.loads(response.text)
    print(output)
    matches = output['profanity']['matches']
    if len(matches) == 0:
      return False
    topics = ', '.join(map(lambda match: match['type'], matches))
    print(topics)
    return f'Found {topics} content in the application'

# check_profanity('s3x smoke alcohol n3gro fifth street')
# check_profanity('s3x fifth street')