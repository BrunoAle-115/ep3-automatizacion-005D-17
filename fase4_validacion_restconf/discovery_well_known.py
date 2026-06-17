import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Esta es la ruta estándar para descubrir servicios RESTCONF
url = "https://192.168.10.1/.well-known/host-meta"
auth = HTTPBasicAuth('cisco', 'cisco123!')
headers = {'Accept': 'application/xrd+xml'}

response = requests.get(url, auth=auth, headers=headers, verify=False)
print(f"Status Code: {response.status_code}")
print(response.text)
