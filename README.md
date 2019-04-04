# Retrieving passwords via AIM

./cyberark-getpwd.py -a APPLICATION_ACCOUNT -s SAFE -u ACCOUNT

# Remove this two lines in PRODUCTION
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
