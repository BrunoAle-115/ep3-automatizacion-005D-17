import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Esta es la ruta raíz de los modelos YANG en IOS-XE
url = "https://192.168.10.1/restconf/data/"
auth = HTTPBasicAuth('cisco', 'cisco123!')
headers = {'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=auth, headers=headers, verify=False)
print(f"Status Code: {response.status_code}")
print(response.json())
