import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()
AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}
events_responses = requests.get("https://www.thebluealliance.com/api/v3/event/2024ausc",
                                     params=parameters)
events = json.loads(events_responses.content)
print(events)