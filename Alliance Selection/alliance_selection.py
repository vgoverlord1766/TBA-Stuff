import requests
from dotenv import load_dotenv
import os
import json

weeks_year = 2024


def get_events(year):
    events_responses = requests.get("https://www.thebluealliance.com/api/v3/events/" + str(year),
                                    params=parameters)
    events = json.loads(events_responses.content)

    events_dict_by_week = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], "other": []}
    for event in events:
        print(1)
        if event["week"]:
            events_dict_by_week[event["week"]].append(event['key'])
        else:
            events_dict_by_week["other"].append(event['key'])

    events_dict_json_object = json.dumps(events_dict_by_week, indent=4)

    with open("events.json", "w") as outfile:
        outfile.write(events_dict_json_object)


def get_event_alliances(event):
    event_alliances_response = requests.get("https://www.thebluealliance.com/api/v3/event/" + event + "/alliances",
                                            params=parameters)
    event_alliances = json.loads(event_alliances_response.content)
    if event_alliances:
        print(event + ":")
        for alliance in event_alliances:
            captain = alliance["picks"][0][3:]
            first_pick = alliance["picks"][1][3:]
            second_pick = alliance["picks"][2][3:]
            elimination = alliance["status"]["double_elim_round"]
            if elimination == "Finals" and alliance["status"]["status"] == "won":
                elimination = "Won"

            print('{} {:<17} {:<18} {:<18} {}'.format(alliance["name"] + ": ", "Captain: " + captain,
                                                      "1st pick: " + first_pick,
                                                      "2nd pick: " + second_pick, elimination))
    else:
        print(event + " has not had alliance selection yet!")


def get_week_event_alliances(week):
    events_object = open('events.json')
    events_by_week = json.load(events_object)
    events = events_by_week[week]
    for event in events:
        get_event_alliances(event)


load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}


print("Enter a 2024 week # or any year's event code (e.g. \"2023mabos\")")
print("To change the year that has its events by week stored, change the \"weeks_year\" variable and enter reset")
print("There is a bug in the TBA API events sometimes do not come back with the right week. Try putting in the"
      " event code if it doesn't show up under its week or enter \"other\" to show unsorted events.")

user_input = input()

if user_input == "reset":
    get_events(weeks_year)
elif user_input in ["1", "2", "3", "4", "5", "6", "other"]:
    get_week_event_alliances(user_input)
else:
    get_event_alliances(user_input)
