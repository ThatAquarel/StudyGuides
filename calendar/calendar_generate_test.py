from icalendar import Calendar, Event
from datetime import datetime, timedelta
from pytz import UTC  # timezone
import uuid

# Create a calendar
cal = Calendar()

# Add some properties to the calendar
cal.add('prodid', '-//My Calculus Schedule//mxm.dk//')
cal.add('version', '2.0')

# Event details
event_name = "Calculus Class"
event_start_time = datetime(2024, 8, 26, 10, 0, 0, tzinfo=UTC)  # Example start date
event_end_time = event_start_time + timedelta(hours=1)
event_location = "Room 101"
event_color = "red"

# Create the event
event = Event()
event.add('summary', event_name)
event.add('dtstart', event_start_time)
event.add('dtend', event_end_time)
event.add('location', event_location)
event.add('uid', str(uuid.uuid4()))
event.add('rrule', {'freq': 'weekly', 'byday': 'MO'})

# Custom property for color (not standardized, may not be supported by all clients)
event.add('X-APPLE-CALENDAR-COLOR', event_color)

# Add event to the calendar
cal.add_component(event)

# Write to .ics file
with open('calculus_class_schedule.ics', 'wb') as f:
    f.write(cal.to_ical())

print("ICS file created successfully.")