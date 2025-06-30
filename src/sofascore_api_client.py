import os
import requests

class SofaScoreAPIClient:
    def __init__(self):
        """
        Initializes the SofaScore API client with the necessary URL, query parameters, and headers
        """
        self.url = 'https://sofascore.p.rapidapi.com/teams/get-next-matches'
        self.querystring = {'teamId': os.getenv('TEAM_ID'), 'pageIndex': '0'}
        self.headers = {
            'x-rapidapi-key': os.getenv('RAPID_API_KEY'),
            'x-rapidapi-host': 'sofascore.p.rapidapi.com'
        }

    def get_events(self):
        """
        Fetches the next matches for the specified team from the SofaScore API
        Returns:
            list: A list of events (matches) for the team
        """
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        events = response.json().get('events', [])
        return events