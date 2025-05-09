import os

import requests

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    API_KEY = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    print(f"Token value: {API_KEY}")
    
    headers = {
        'Authorization': f"Bearer {API_KEY}"
    }
    r = requests.get("https://jedi.enterprise.corellium.com/api/v1/instances", headers=headers)
    if r.status_code == 200:
        data = r.json()
        device_name = data[0]['name']
        print(f'Name of first device: {device_name}')
