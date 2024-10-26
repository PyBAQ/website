"""Descarga eventos usando Meetup api"""

import json

import requests

# NOTE: This endpoint no requires authentication, but this API is deprecated

EVENTS_URL = 'https://api.meetup.com/pythonbaq/events?&sign=true&photo-host=secure'
PAST_EVENTS_URL = EVENTS_URL + '&page=200&fields=featured_photo&desc=true&status=past'
FUTURE_EVENTS_URL = EVENTS_URL + '&page=3&fields=featured_photo'

past_events_request = requests.get(PAST_EVENTS_URL, timeout=30000)
future_events_request = requests.get(FUTURE_EVENTS_URL, timeout=30000)


meetup_responses = json.dumps({
    "past_events": past_events_request.json(),
    "future_events": future_events_request.json()
})

with open("databags/meetup.json", "w", encoding="utf-8") as outfile:
    outfile.write(meetup_responses)
