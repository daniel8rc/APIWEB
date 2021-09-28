from datetime import datetime, timedelta
import requests
import os
import dotenv

class Api():
    def __init__(self):
        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': os.environ.get("API_KEY")
        }
        self.yesterday = datetime.now() - timedelta(days=1)
        print(self.yesterday)
        self.year = self.yesterday.year
        self.yesterday_str = self.yesterday.strftime("%Y-%m-%d")

    def get_latest_data(self):
        url = "https://v3.football.api-sports.io/fixtures?season=%i&date=%s" % (self.year, self.yesterday_str)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            print(response.json())

if __name__ == "__main__":
    env_file = ".env"

    if os.path.isfile(env_file):
        dotenv.load_dotenv(env_file)
        api = Api()
        api.get_latest_data()
