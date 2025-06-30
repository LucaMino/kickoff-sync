import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleCalendarClient:
    def __init__(self, credentials_file='src/google-key.json', scopes=None):
        """
        Initializes the Google Calendar client with the specified credentials and scopes
        Args:
            credentials_file (str): Path to the credentials file. Default is 'src/google-key.json'
            scopes (list[str], optional): List of access scopes. If None, default scopes will be used
        """
        if scopes is None:
            scopes = ['https://www.googleapis.com/auth/calendar']
        self.credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def create_event(self, event_data):
        """
        Creates a new event in the Google Calendar
        Args:
            event_data (dict): A dictionary containing the event details
        Returns:
            dict: The created event
        """
        event = self.service.events().insert(calendarId=os.getenv('CALENDAR_ID'), body=event_data, sendUpdates='all').execute()
        return event

    def update_event(self, event_id, event_data):
        """
        Updates an existing event in the Google Calendar
        Args:
            event_id (str): The ID of the event to update
            event_data (dict): A dictionary containing the updated event details
        Returns:
            dict: The updated event
        """
        event = self.service.events().update(calendarId=os.getenv('CALENDAR_ID'), eventId=event_id, body=event_data).execute()
        return event

    def search_event(self, ical_uid):
        """
        Searches for an event in the Google Calendar by its iCalUID
        Args:
            ical_uid (str): The iCalUID of the event to search for
        Returns:
            dict: The found event, or None if not found
        """
        events = self.service.events().list(calendarId=os.getenv('CALENDAR_ID'), iCalUID=ical_uid).execute()
        items = events.get('items', [])
        return items[0] if items else None