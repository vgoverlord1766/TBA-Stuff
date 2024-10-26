import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

finalist_count = 0

awards_response = requests.get("https://www.thebluealliance.com/api/v3/team/frc2877/awards",
                                params=parameters)
awards = json.loads(awards_response.content)

for award in awards:
    if award["award_type"] == 2:
        finalist_count += 1

print(finalist_count)

