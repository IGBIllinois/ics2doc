#! python
import datetime
from icalevents.icalevents import events
from pytz import timezone
import config
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

# Calculate last week and this week
now = datetime.datetime.now()
tz = timezone('US/Central')
today = datetime.datetime(year=now.year, month=now.month, day=now.day, tzinfo=tz)
last_week = today + datetime.timedelta(weeks=-1)
next_week = today + datetime.timedelta(weeks=1, days=1)
six_months = today + datetime.timedelta(days=180)

last_week_events = []
next_week_events = []
six_months_events = []
for calendar in config.calendars:
    print("Fetching events from '{:}'...".format(calendar['title']))
    no_recurrence = False
    if 'no_recurrence' in calendar and calendar['no_recurrence']:
        no_recurrence = True
    # Fetch events
    print("Fetching last week's events...")
    last_week_events.append(events(url=calendar['url'], start=last_week, end=today, no_recurrence=no_recurrence))
    print("Fetching this week's events...")
    next_week_events.append(events(url=calendar['url'], start=today, end=next_week, no_recurrence=no_recurrence))
    print("Fetching upcoming events...")
    six_months_events.append(events(url=calendar['url'], start=next_week, end=six_months, no_recurrence=no_recurrence))

print("Generating report...")
env = Environment(loader=FileSystemLoader('templates'), autoescape=select_autoescape(['html']))
template = env.get_template('index.html')
html_string = template.render(date=today, last_week_events=last_week_events, next_week_events=next_week_events,
                              six_months_events=six_months_events, tz=tz,
                              allday_correction=datetime.timedelta(days=-1), calendars=config.calendars)

HTML(string=html_string).write_pdf("report.pdf")
