import tweepy
import json
import datetime

def twitter_oauth():
    with open('data/auth.json', 'r') as f:
        data = json.load(f)
    try:
        auth = tweepy.OAuthHandler(data['twitter_api_key'], data['twitter_api_secret_key'])
        auth.set_access_token(data['twitter_access_token'], data['twitter_access_token_secret'])
        return auth
    except:
        return None

def main():
    with open('data/stats.json', 'r') as f:
        stats = json.load(f)
    oauth = twitter_oauth()
    api = tweepy.API(oauth)
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    image_path = f"pics/{date}.png"
    status = f"I've biked {round(stats['distance'] / 1000, 2)}km and climbed {round(stats['elevation'], 2)}m over {stats['rides']} bike rides so far."
    api.update_with_media(image_path, status)