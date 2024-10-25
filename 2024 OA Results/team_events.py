import requests
from dotenv import load_dotenv
import os
import json
import time


def get_team_events():
    start = time.time()
    load_dotenv()

    AUTH_KEY = os.getenv('AUTH_KEY')
    parameters = {
        "X-TBA-Auth-Key": AUTH_KEY
    }
    events_responses = requests.get("https://www.thebluealliance.com/api/v3/events/2024/keys",
                                         params=parameters)
    events = json.loads(events_responses.content)

    events_dict = {}
    events_dict_by_week = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for event in events:
        events_dict[event] = []

    print(events_dict)

    with open('2024 OA Teams', 'r') as team_list_file:
        team_list = team_list_file.read().splitlines()

    for team in team_list:
        team_events_responses = requests.get("https://www.thebluealliance.com/api/v3/team/frc" + team + "/events/2024/keys",
                                          params=parameters)
        team_events = json.loads(team_events_responses.content)
        for team_event in team_events:
            events_dict[team_event].append(team)
        print("1")

    for event in events_dict:
        event_responses = requests.get("https://www.thebluealliance.com/api/v3/event/" + event,
                                       params=parameters)
        event_data = json.loads(event_responses.content)
        print(event)
        print(event_data)
        print(event_data["week"])
        # events_dict[event].insert(0, event_data["week"])
        events_dict_by_week[event_data["week"]].append(events_dict[event])
        print(events_dict_by_week[event_data["week"]])
        print("2")

    end = time.time()
    print("Execution time of the program is- ", end-start)
    print(events_dict)

    events_dict_json_object = json.dumps(events_dict_by_week, indent=4)

    with open("events.json", "w") as outfile:
        outfile.write(events_dict_json_object)



