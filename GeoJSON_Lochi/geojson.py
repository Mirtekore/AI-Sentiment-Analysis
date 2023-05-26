import json
import geojson

with open("aitweets.json") as f:
    data = json.load(f)

geojson = {
    'type': 'FeatureCollection',
    'docs': []
}


for key, value in data.items():
    feature = {
        'type': 'Feature',
        'properties': value,
        'geometry': {
            'type': 'Point',
            'coordinates': [
                (value['geo']['bbox'][0] + value['geo']['bbox'][2]) / 2,
                (value['geo']['bbox'][1] + value['geo']['bbox'][3]) / 2
            ]
        }
    }
    geojson['features'].append(feature)

with open('geojson_file.json', 'w') as f:
    json.dump(geojson, f)


with open('geojson_file.json') as f:
    geojson_data = json.load(f)
print(geojson_data)

