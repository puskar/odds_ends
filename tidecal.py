#!/usr/bin/python3

import requests
import json
import pprint
import time
import datetime
from icalendar import Calendar, Event


# {
#     "predictions": [
#         {
#             "t": "2018-06-27 05:50",
#             "type": "L",
#             "v": "-0.031"
#         }
#     ]
# }

#cal['dtstart'] = '20050404T080000'

begindate = datetime.date.today().strftime('%Y%m%d')
enddate = datetime.date.today() +  datetime.timedelta(days=90)
enddate = enddate.strftime('%Y%m%d')

#8469198 - Stamford Harbor, CT
#8517394 - Barren Island, Rockaway Inlet
#8532337 - Belmar, NJ

payload = {'product': 'predictions', 'application': 'NOS.COOPS.TAC.WL', 'begin_date': begindate, 'end_date': enddate, 'datum': 'MLLW', 'station': '8469198', 'time_zone': 'GMT', 'units': 'english', 'interval': 'hilo', 'format': 'json'}

r = requests.get('https://tidesandcurrents.noaa.gov/api/datagetter', params=payload)

tides = r.json()

cal = Calendar()
#cal.add('prodid', '-//my tide script')
#cal.add('version', '0.99')

for forecast in tides['predictions']:
  time = forecast['t']
  tide = forecast['type']
  height = forecast['v']
  d = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M").strftime('%Y%m%dT%H%M00Z')
  if tide == 'H':
    longt = "High Tide"
  elif tide == 'L':
    longt = "Low Tide"
  event = Event()
  event['dtstart'] = d
  event['summary'] = longt
  event['dtend'] = d
  event['location'] = """Greenwich Point Park
58 Tods Driftway
Old Greenwich, CT  06870
United States"""
  cal.add_component(event)

print(cal.to_ical().decode('utf-8'))
