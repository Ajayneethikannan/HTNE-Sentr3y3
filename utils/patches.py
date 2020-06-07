import requests

def increment(app, time):
    
    response = requests.patch(f'http://localhost:8000/apps/{app["id"]}/', json={
        'time_today': app['time_today'] + time,
        'week_time': app['week_time'] + time,
        'total_time': app['total_time'] + time
    })
    return response

def set_warning(app, warning):

    response = requests.patch(f'http://localhost:8000/apps/{app["id"]}/', json={
        'warning': warning
    })
    return response
