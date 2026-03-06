import urllib.request
import os

domains = {
    "osmania": "osmania.ac.in",
    "hyderabad": "uohyd.ac.in",
    "uri": "uri.edu",
    "harvard": "harvard.edu",
    "mit": "mit.edu",
    "dell": "dell.com",
    "prudential": "prudential.com",
    "dnb": "dnb.com",
    "db": "db.com",
    "powerlytics": "powerlytics.com",
    "datacamp": "datacamp.com",
    "fullsail": "fullsail.edu",
    "wpi": "wpi.edu"
}

os.makedirs("images", exist_ok=True)

for name, domain in domains.items():
    url = f"https://logo.clearbit.com/{domain}"
    out_path = f"images/{name}_logo.png"
    print(f"Trying {name} at {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(out_path, 'wb') as f:
            f.write(response.read())
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
