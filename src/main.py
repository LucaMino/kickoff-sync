import pytz
from datetime import datetime, timedelta
from sofascore_api_client import SofaScoreAPIClient
from google_calendar_client import GoogleCalendarClient

def main():
    print('Start script')
    # retrieve events from SofaScore API
    sofascore = SofaScoreAPIClient()
    events = sofascore.get_events()

    print(f'Found {len(events)} events at {datetime.now(pytz.timezone("Europe/Rome")).isoformat()}')

    for event in events:
        # convert startTimestamp to datetime object
        dt = datetime.fromtimestamp(event['startTimestamp'], pytz.timezone('Europe/Rome'))
        # generate unique iCalUID
        ical_uid = f"{event['id']}@kickoffsync.com"
        # create calendar event data
        event_data = {
            'summary': event['homeTeam']['name'] + ' vs ' + event['awayTeam']['name'] + ' - ' + event['season']['name'],
            'start': {
                'dateTime': dt.isoformat(),
                'timeZone': 'Europe/Rome',
            },
            'end': {
                'dateTime': (dt + timedelta(hours=2)).isoformat(),
                'timeZone': 'Europe/Rome',
            },
            'iCalUID': ical_uid
        }
        # create Google Calendar instance
        calendar = GoogleCalendarClient()
        # search if the event already exists
        old_event = calendar.search_event(ical_uid)
        # if no existing event, create a new one
        if old_event is None:
            calendar.create_event(event_data)
            print(f"Event '{event_data['summary']}' created")
        else:
            # check if the existing event needs to be updated
            if old_event['summary'] != event_data['summary'] or old_event['start']['dateTime'] != event_data['start']['dateTime']:
                # update existing event
                calendar.update_event(old_event['id'], event_data)
                print(f"Event '{event_data['summary']}' updated")

    print('End script')

if __name__ == '__main__':
    main()