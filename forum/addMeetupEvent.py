import requests
import json

def create_meetup_event(api_key, group_urlname, event_data):

    print("Let's Begin")
    url = f"https://api.meetup.com/{group_urlname}/events"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(event_data))

    if response.status_code == 201:
        print("Event created successfully!")
        event_info = response.json()
        print(f"Event ID: {event_info['id']}")
    else:
        print(f"Failed to create event. Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Example usage
api_key = 'ENTER_YOUR_MEETUP_API_KEY'
group_urlname = 'ENTER_YOUR_GROUP_URLNAME'
event_data = {
    "name": "Automated Coffee For All",
    "description": "We are having an automation coffee blowout",
    "time": 1672531200000,  # Example timestamp in milliseconds
    "duration": 7200000,    # Duration in milliseconds (2 hours)
    "venue_id": 123456,     # Example venue ID
    "how_to_find_us": "Look for the big coffee sign!",
    "rsvp_limit": 50,
    "event_hosts": [12345678],  # Example host member ID
    "fee": {
        "amount": 5.00,
        "currency": "USD",
        "accepts": "paypal"
    }
}

create_meetup_event(api_key, group_urlname, event_data)
