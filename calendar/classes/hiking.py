import os

import uuid
from icalendar import Calendar, Event
from datetime import datetime, timedelta

cal = Calendar()

cal.add("prodid", "-//" "//mxm.dk//")
cal.add("version", "2.0")


def new_class(name, location, weekday, hour, minute, hour_d, minute_d, count):
    event_start_time = datetime(2024, 8, 26 + weekday, hour, minute, 0)
    event_end_time = event_start_time + timedelta(hours=hour_d, minutes=minute_d)

    event = Event()
    event.add("summary", name)
    event.add("dtstart", event_start_time)
    event.add("dtend", event_end_time)
    event.add("location", location)
    event.add("uid", str(uuid.uuid4()))
    event.add("rrule", {"freq": "daily", "interval": 14, "count": count})

    return event


cal.add_component(new_class("Day Hiking", "3F.37", 0, 18, 0, 2, 0, 2))
cal.add_component(new_class("Day Hiking", "0H.1", 2, 18, 0, 2, 0, 2))


file = os.path.basename(__file__)
filename = os.path.splitext(file)[0]

with open(f"calendar/classes/{filename}.ics", "wb") as f:
    f.write(cal.to_ical())
