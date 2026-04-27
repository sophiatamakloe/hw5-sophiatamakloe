from datetime import datetime
from zoneinfo import ZoneInfo

timezones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Accra": "Africa/Accra",
    "Los Angeles": "America/Los_Angeles"
}

base_city = input("Enter base city: ")
meeting_time = input("Enter time (YYYY-MM-DD HH:MM): ")

dt = datetime.strptime(meeting_time, "%Y-%m-%d %H:%M")
base_dt = dt.replace(tzinfo=ZoneInfo(timezones[base_city]))

print("\nMeeting Time Conversions:\n")

for city, tz in timezones.items():
    converted = base_dt.astimezone(ZoneInfo(tz))
    hour = converted.hour

    status = ""
    if hour < 8 or hour > 18:
        status = " (outside business hours)"

    print(f"{city}: {converted.strftime('%Y-%m-%d %I:%M %p')}{status}")
