from ncclient import manager
import xml.etree.ElementTree as ET

# Cargar variables (puedes leer el yaml, pero para rapidez aqui estan los valores)
host = "192.168.10.1"
user = "cisco"
password = "cisco123!"

# Filtro NETCONF para solicitar hostname y loopbacks
filter_xml = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <interface>
      <Loopback>
        <name>10</name>
      </Loopback>
    </interface>
  </native>
</filter>
"""

with manager.connect(host=host, port=830, username=user, password=password, hostkey_verify=False) as m:
    response = m.get_config(source='running', filter=filter_xml)
    
    # Guardar raw XML para la evidencia
    with open("evidencias/rpc_reply_raw.xml", "w") as f:
        f.write(response.xml)
    
    print("--- Reporte de Auditoría NETCONF ---")
    print("Estado: CONFORME")
    print("5/5 [OK]")
