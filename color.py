import sys
import platform

colors = True
machine = sys.platform.lower()
checkplatform = platform.platform()

if machine.startswith(('os', 'darwin', 'ios', 'win')):
    colors = False
if not colors:
    end = red = white = green = yellow = ""
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'