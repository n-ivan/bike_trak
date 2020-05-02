import functions.draw_paths as dp
import functions.strava_api as sa
import functions.to_geojson as gj
import functions.tweet as tweet

def main():
    sa.get_activities()
    gj.activities_to_geojson()
    dp.draw_to_png()
    dp.draw_to_png_fixed()
    tweet.main()
    print('Posted a tweet')

main()