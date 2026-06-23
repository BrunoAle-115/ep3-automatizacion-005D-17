import requests
import json
import yaml
import os
import socket
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. Cargar variables reales
with open("../vars/vars_005D-17.yaml", 'r') as file:
    vars_data = yaml.safe_load(file)

auth = (vars_data['router']['usuario'], vars_data['router']['password'])
router_ip = "192.168.10.1"
headers = {'Accept': 'application/yang-data+json'}

# 2. Crear directorios exigidos por la rúbrica
os.makedirs("evidencias/responses", exist_ok=True)

# 3. Metadatos
print("=== METADATOS DE EJECUCIÓN ===")
print("Script: validacion_restconf_005D-17.py")
print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Hostname VM: {socket.gethostname()}")
print("==============================\n")

print("--- Iniciando Auditoría RESTCONF ---")

# 4. Endpoints oficiales según rúbrica
endpoints = {
    "hostname": {
        "url": f"https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/hostname",
        "file": "get_hostname.json",
        "expected": vars_data['cliente']['hostname']
    },
    "loopback": {
        "url": f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback10",
        "file": "get_loopback.json",
        "expected": vars_data['router']['loopback_ip']
    },
    "interfaces": {
        "url": f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
        "file": "get_interfaces.json",
        "expected": vars_data['router']['descripcion_wan']
    },
    "ntp": {
        "url": f"https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/ntp",
        "file": "get_ntp.json",
        "expected": vars_data['router']['ntp_server']
    }
}

criterios_ok = 0

# 5. Ejecutar consultas y guardar JSONs
for key, data in endpoints.items():
    try:
        resp = requests.get(data["url"], auth=auth, headers=headers, verify=False)
        if resp.status_code == 200:
            json_data = resp.json()
            
            # Guardar el JSON específico
            with open(f"evidencias/responses/{data['file']}", "w") as f:
                json.dump(json_data, f, indent=4)
            
            # Validar si el valor esperado está en la respuesta
            if str(data["expected"]) in json.dumps(json_data):
                print(f"[OK] {key.capitalize()}: {data['expected']}")
                criterios_ok += 1
            else:
                print(f"[FAIL] {key.capitalize()} (Valor distinto)")
        else:
             print(f"[FAIL] {key.capitalize()} (Status HTTP: {resp.status_code})")
    except Exception as e:
        print(f"[FAIL] {key.capitalize()} (Error de red)")

# 6. Imprimir resultado global
print("\n--- Resultado Final ---")
if criterios_ok == 4:
    print("4/4 [OK] - CONFORME")
else:
    print(f"{criterios_ok}/4 [OK] - NO CONFORME")
