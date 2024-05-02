import requests
from icalendar import Calendar, Event
import re
from flask import Flask, make_response, render_template


flask_app = Flask("ghsathletics")


url = "https://www2.arbitersports.com/ICal/School/schedule.ics?id=cHHWgTXR%2b%2fvlYfnDlphDuQ%3d%3d"


@flask_app.route("/ghscal/", methods=['GET'], defaults={'part1': '', 'part2': '', 'part3': ''})
@flask_app.route("/ghscal/<string:part1>", methods=['GET'], defaults={'part2': '', 'part3': ''})
@flask_app.route("/ghscal/<string:part1>/<string:part2>", methods=['GET'], defaults= {'part3': ''})
@flask_app.route("/ghscal/<string:part1>/<string:part2>/<string:part3>", methods=['GET'])


def getcal(part1, part2, part3):
    cal = Calendar.from_ical(requests.get(url).text)

    #print(cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())

    match = [part1, part2, part3]
    match = [element.lower() for element in match]

    newcal = Calendar()

    for component in cal.walk(name="VEVENT"):
        desc = component.get("description").replace("\n", " ").lower().split()
        
        #print(f'match={match} desc={desc}')
        if all(any(sub in string for string in desc) for sub in match):
            component.get("description")
            newcal.add_component(component)
            
    newcal.add('X-WR-CALNAME', f'{part1.title()} {part2.title()} {part3.title()}')
  

    response = make_response(newcal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())
    response.headers['Content-Type'] = 'text/calendar'
    response.headers['Content-Disposition'] = f'inline; filename="{part1.title()}{part2.title()}{part3.title()}.ics"'
    return(response)

#getcal("boys", "freshmen", "lacrosse")

  
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8080, debug=True)