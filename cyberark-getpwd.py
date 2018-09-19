#!/usr/bin/python
import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import sys

url = "https://sam-development/aimwebservice/api/Accounts"

def help():
  global AppID
  global Safe
  global Username
  parser = argparse.ArgumentParser(
        description="\nEXAMPLE: ./%(prog)s -a WSAUTOCOP -s Weblogic -u weblogic")
  parser.add_argument("-a", "--appid", help="Specify the Application Account", type=str)
  parser.add_argument("-s", "--safe", help="Specify the Safe", type=str)
  parser.add_argument("-u", "--username", help="Specify the username for retrieving the password associated", type=str)

  args = parser.parse_args()
  if args.appid is None or args.safe is None or args.username is None:
    parser.print_help()
    sys.exit(1)
  else:
    pass

  AppID = args.appid
  Safe = args.safe
  Username = args.username
help()

# Making the call
x = {"AppID":AppID,"Safe":Safe,"Folder":"Root","UserName":Username}
headers = {'content-type': 'application/json'}
response = requests.request("GET", url, headers=headers, params=x, verify=False)
username = response.json().get('UserName')
password = response.json().get('Content')
print(password)
