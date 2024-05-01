import requests
from icalendar import Calendar, Event
import re
from flask import Flask, make_response, render_template


flask_app = Flask("ghsathletics")


url = "https://www2.arbitersports.com/ICal/School/schedule.ics?id=cHHWgTXR%2b%2fvlYfnDlphDuQ%3d%3d"


@flask_app.route("/ghscal/<part1>/<part2>/<part3>", methods=['GET'])

def getcal(part1, part2, part3):
    cal = Calendar.from_ical(requests.get(url).text)

    #print(cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())

    newcal = Calendar()

    for component in cal.walk(name="VEVENT"):
        if re.search('.*' + part1 + '*', component.get("description"), flags=re.I) and re.search('.*' + part2 + '*', component.get("description"), flags=re.I) and re.search('.*' + part3 + '*', component.get("description"), flags=re.I):
            component.get("description")
            newcal.add_component(component)
            #print(component.to_ical().decode("utf-8").replace('\r\n', '\n').strip())
            
    newcal.add('X-WR-CALNAME', f'{part1} {part2} {part3}')
  

    response = make_response(newcal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())
    response.headers['Content-Type'] = 'text/calendar'
    response.headers['Content-Disposition'] = f'inline; filename="{part1}{part2}{part3}.ics"'
    return(response)

#getcal("boys", "freshmen", "lacrosse")

  
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8080, debug=True)