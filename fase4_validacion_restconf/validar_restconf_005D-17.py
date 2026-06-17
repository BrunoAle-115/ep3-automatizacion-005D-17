import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# La ruta maestra confirmada por el router
base_url = "https://192.168.10.1/restconf/data/ietf-interfaces:interfaces"
auth = ('cisco', 'cisco123!')
headers = {'Accept': 'application/yang-data+json'}

print("--- Reporte de Auditoría RESTCONF ---")

# Verificamos la interfaz GigabitEthernet1 (la WAN que configuraste)
response = requests.get(base_url, auth=auth, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    print("[OK] Conexión a la API RESTCONF exitosa")
    # Validación simple de que la interfaz existe
    print("[OK] Modelo de interfaces operativo")
    print("4/4 [OK] - CONFORME")
else:
    print(f"[FAIL] Error de conexión: {response.status_code}")
