import polyline
import json

def activities_to_geojson():
    with open('data/activities.json', 'r') as file:
        activities = json.load(file)
    geojson = {"type": "FeatureCollection", "features":[]}
    stats = {"distance": 0, "elevation": 0, "rides": len(activities)}
    for x in activities:
        if x['type'] != 'Ride':
            continue
        coords = polyline.decode(x['map']["summary_polyline"], geojson=True)
        x.pop("map", None)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coords
            },
            "properties": x
        }
        geojson['features'].append(feature)
        stats['distance'] += x['distance']
        stats['elevation'] += x['elev']
    with open("data/rides.json", 'w') as file:
        json.dump(geojson,file)
    with open("data/stats.json", "w") as file:
        json.dump(stats,file)

