from dataclasses import dataclass
import requests
import config


@dataclass
class BoredAPI:
    url: str = config.API_URL

    def get_activity(self, **params):
        activity = requests.get(
            url=self.url, 
            params=params
        )

        if activity.status_code == 200:
            return activity.json()
        
        return False
