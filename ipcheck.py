#!/usr/bin/python3

from pathlib import Path
import subprocess
import requests

home = str(Path.home())

file = home + "/.wan_ip"

r = requests.get("https://ipecho.net/plain")

path = Path(file)

if path.is_file():

  f = open(file, "r+")
  old_ip = f.read()
  if old_ip == r.text:
    exit()
  f.seek(0)
  f.truncate()
else:

 f = open(file, "w")


f.write(r.text)
message = "New ip is " + r.text + "\nOld ip is " + old_ip
proc = subprocess.run(['terminal-notifier', '-message', message , '-title', 'Network update', '-subtitle', 'WAN IP changed', '-timeout', '0'])
print("the commandline is {}".format(proc.args))
f.close()
