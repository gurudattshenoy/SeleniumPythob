import json
with open('/home/acme/selenium/SeleniumPython/Configurations/browser_conf.json') as f:
    data = json.load(f)
from collections import namedtuple

driver_conf = namedtuple('browser', data.keys())(**data)



