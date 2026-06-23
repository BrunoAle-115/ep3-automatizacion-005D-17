import socket
from datetime import datetime
from ncclient import manager
import xml.etree.ElementTree as ET
import yaml

# 1. Cargar tus variables reales
with open("../vars/vars_005D-17.yaml", 'r') as file:
    vars_data = yaml.safe_load(file)

router_ip = "192.168.10.1" # Mantenemos la IP que te funcionó en el laboratorio
user = vars_data['router']['usuario']
password = vars_data['router']['password']

expected_hostname = vars_data['cliente']['hostname']
expected_ntp = vars_data['router']['ntp_server']
expected_loop_ip = vars_data['router']['loopback_ip']
expected_loop_mask = vars_data['router']['loopback_mask']
expected_wan_desc = vars_data['router']['descripcion_wan']

# 2. Imprimir Metadatos requeridos por la rúbrica
print("=== METADATOS DE EJECUCIÓN ===")
print("Script: validacion_netconf_005D-17.py")
print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Hostname VM: {socket.gethostname()}")
print("==============================\n")

# 3. Filtro XML para el modelo Cisco-IOS-XE-native
filter_xml = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <ntp/>
    <interface>
      <Loopback>
        <name>10</name>
      </Loopback>
      <GigabitEthernet>
        <name>1</name>
      </GigabitEthernet>
    </interface>
  </native>
</filter>
"""

print("--- Iniciando Auditoría NETCONF ---")

# Conexión con los parámetros exigidos por la pauta
with manager.connect(host=router_ip, port=830, username=user, password=password, 
                     hostkey_verify=False, allow_agent=False, look_for_keys=False) as m:
    
    # Ejecutar get_config
    reply = m.get_config(source='running', filter=filter_xml)
    xml_data = reply.xml
    
    # Guardar el XML crudo en la ruta exigida
    with open("evidencias/rpc_reply_raw.xml", "w") as f:
        f.write(xml_data)
        
    # 4. Extracción y comparación básica
    criterios_ok = 0
    
    # Hostname
    if f"<hostname>{expected_hostname}</hostname>" in xml_data:
        print(f"[OK] Hostname: {expected_hostname}")
        criterios_ok += 1
    else:
        print("[FAIL] Hostname")

    # IP Loopback
    if f"<address>{expected_loop_ip}</address>" in xml_data:
        print(f"[OK] IP Loopback: {expected_loop_ip}")
        criterios_ok += 1
    else:
        print("[FAIL] IP Loopback")

    # Máscara Loopback
    if f"<mask>{expected_loop_mask}</mask>" in xml_data:
        print(f"[OK] Máscara Loopback: {expected_loop_mask}")
        criterios_ok += 1
    else:
        print("[FAIL] Máscara Loopback")

    # Descripción WAN
    if f"<description>{expected_wan_desc}</description>" in xml_data:
        print(f"[OK] Descripción WAN: {expected_wan_desc}")
        criterios_ok += 1
    else:
        print("[FAIL] Descripción WAN")

    # Servidor NTP
    if expected_ntp in xml_data:
        print(f"[OK] Servidor NTP: {expected_ntp}")
        criterios_ok += 1
    else:
        print("[FAIL] Servidor NTP")

    # 5. Imprimir resultado global
    print("\n--- Resultado Final ---")
    if criterios_ok == 5:
        print("5/5 [OK] - CONFORME")
    else:
        print(f"{criterios_ok}/5 [OK] - NO CONFORME")
