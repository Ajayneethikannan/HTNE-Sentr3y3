import requests

def increment(app, time):
    
    response = requests.patch(f'http://localhost:8000/apps/{app["id"]}/', json={
        'time_today': app['time_today'] + time,
        'week_time': app['week_time'] + time,
    })
    return response
