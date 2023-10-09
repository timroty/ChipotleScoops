import requests
import json
from config import load_config

class Restaurant_Service:
    def __init__(self):
        # Configs
        config = load_config()

        self.chipotle_subscription_key: str = config.chipotle_subscription_key
    
    async def search(self, latitude: float, longitude: float):
        url = "https://services.chipotle.com/restaurant/v3/restaurant"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.chipotle_subscription_key,
            'Origin': 'https://www.chipotle.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.chipotle.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }

        payload = {
            "latitude": latitude,
            "longitude": longitude,
            "radius": 80467,
            "restaurantStatuses": ["OPEN", "LAB"],
            "conceptIds": ["CMG"],
            "orderBy": "distance",
            "orderByDescending": False,
            "pageSize": 10,
            "pageIndex": 0,
            "embeds": {
                "addressTypes": ["MAIN"]
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"Error": f"Request failed {response.status_code}"}