import requests
import json

##Update NTP Server List


Tenant="Enter Tenant ID"
SiteID="Enter Site ID"
ElementID="Enter Element ION ID"
Authtoken="Enter Auth token"
NEW_NTP_SERVER="Enter NTP Server x.x.x.x"

url = "https://api.elcapitan.cloudgenix.com/v2.0/api/tenants/{}/elements/{}/ntp".format(Tenant, ElementID)


headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': Authtoken
}

####Get the WAN Interface Config
GET_NTP_CONFIG = requests.request("GET", url, headers=headers)

###Convert to DICTIONARY
Jsonformatted = GET_NTP_CONFIG.json()

###Add changed value
NewNTP = {'ntp_servers': [{"host":NEW_NTP_SERVER,"version":4,"min_poll":6,"max_poll":10}]}
Jsonformatted.update(NewNTP)

##Format back to type to import back in
Serialized_JSON_DATA = json.dumps(Jsonformatted)

##PUTTING DATA BACK
response = requests.request("PUT", url, headers=headers, data=Serialized_JSON_DATA)
