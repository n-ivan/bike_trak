import pandas as pd
import requests
import json
import datetime

auth_url = "https://www.strava.com/oauth/token"

activ_url = "https://www.strava.com/api/v3/athlete/activities"

def request_token():
    '''
    Gets the access token when it expires.
    '''
    with open('data/auth.json', 'r') as file:
        data = json.load(file)
    res = requests.post(auth_url, data=data['refresh'], verify=False).json()
    data['access_token'] = res['access_token']
    data['token_expiry'] = res['expires_at']
    with open('data/auth.json', 'w') as file:
        json.dump(data,file)

def get_activities():
    '''
    Gets all activities from strava and formats them.
    '''
    with open('data/auth.json', 'r') as f:
        data = json.load(f)

    if (int(datetime.datetime.utcnow().timestamp()) > data['token_expiry']):
        request_token()
        with open('data/auth.json', 'r') as f:
            data = json.load(f)
    
    page = 1

    header = {'Authorization': f'Bearer {data["access_token"]}'}

    activities = []

    while True:
        param = {'per_page': 200, 'page': page}
        res = requests.get(activ_url, headers=header, params=param)
        data = res.json()
        if (res.status_code != 200 or not data):
            break
        for x in data:
            activities.append({"id": x["id"], "name": x["name"], "type": x["type"], "distance": x["distance"], "elev": x["total_elevation_gain"], "map": x["map"]})
        page+=1

    with open('data/activities.json', 'w') as file:
        json.dump(activities, file)