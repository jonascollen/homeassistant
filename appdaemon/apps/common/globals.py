from enum import Enum

# Global variables

presence_state = {}
# Change this if you want to change the display name
presence_state["home"] = "Home"
presence_state["just_arrived"] = "Just arrived"
presence_state["just_left"] = "Just left"
presence_state["away"] = "Away"
presence_state["extended_away"] = "Extended away"


PEOPLE = {
    'Jonas': {
        'device_tracker': 'device_tracker.presence_jonas'
    },
    'Malin': {
        'device_tracker': 'device_tracker.malin_s9'
    }
}