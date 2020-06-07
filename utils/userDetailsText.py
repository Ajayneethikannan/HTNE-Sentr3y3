import requests, json


def getUsers():
    users: []

    url = f'http://localhost:8000/users/'
    response = requests.get(url)

    if (response.status_code == 200):
        data = json.loads(response.text)
        users = [(user.get('username'), user.get('id')) for user in data]

    return users



def currentUserDetails(user_id):

    user = ''
    apps = []

    url = f'http://localhost:8000/users/{user_id}/'
    response = requests.get(url)
    
    if (response.status_code != 200):
        displayText = "Server not running, please check the server"
    else:
        data = json.loads(response.text)
        apps = data.get('apps', [])
        user = data.get('username')
        appTitles = [app['title'] for app in apps]
        isUnderAge = data.get('is_underage')
        displayText = "Current user: " + user + "\n\nApps observed: " + ', '.join(appTitles)
    
    return (displayText, user, apps, isUnderAge, response.status_code)