import requests
from dotenv import load_dotenv
import os
import json
import time
import json
import team_events
with open('events.json', 'r') as openfile:
    teams_at_events = json.load(openfile)

if len(teams_at_events) == 0:
    team_events.get_team_events()

print("Enter week #\n")
week_number = input()


