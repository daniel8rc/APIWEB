from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.conf import settings as conf
from football.models import Team
import requests
import os
import dotenv


class Api(APIView):
    def set_configvars(self):
        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': conf.API_KEY
        }
        self.yesterday = datetime.now() - timedelta(days=1)
        self.year = self.yesterday.year
        self.yesterday_str = self.yesterday.strftime("%Y-%m-%d")
        self.league = 2

    def get_latest_data(self):
        self.set_configvars()
        url = "https://v3.football.api-sports.io/fixtures?league=%i&season=%i&date=%s" % (self.league,self.year, self.yesterday_str)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()

    def save_team(self, team):
        print(team)
        Team.objects.get_or_create(
            id=int(team['id']),
            name=team['name'],
            logo=team['logo']
        )

    def save_latest_data(self, latest_data):

        for match in latest_data:
            self.save_team(match['teams']['home'])
            self.save_team(match['teams']['away'])

    def get(self, request):
        latest_data = self.get_latest_data()['response']

        self.save_latest_data(latest_data)

        return Response(latest_data)