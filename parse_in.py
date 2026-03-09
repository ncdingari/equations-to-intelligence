import urllib.request, json
url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries/IND.geo.json"
resp = urllib.request.urlopen(url)
data = json.loads(resp.read().decode('utf-8'))
coords = data['features'][0]['geometry']['coordinates']

def flatten(polys):
    largest = max(polys, key=lambda p: len(p[0]) if isinstance(p[0][0], list) else len(p))
    if isinstance(largest[0][0], list):
        return max(largest, key=len)
    return largest

poly = flatten(coords)
res = [(x, y) for (x, y) in poly]
print("pts =", res[:10], "... total:", len(res))
with open('india_coords.js', 'w') as f:
    f.write('const indiaMapCoords = ' + json.dumps(res) + ';')
