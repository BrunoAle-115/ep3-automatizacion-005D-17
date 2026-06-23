from ncclient import manager
import xml.dom.minidom

host = "192.168.10.1"
user = "cisco"
password = "cisco123!"

# Filtro pidiendo explícitamente hostname, interfaces y NTP
filter_xml = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <ntp/>
    <interface>
      <Loopback>
        <name>10</name>
      </Loopback>
    </interface>
  </native>
</filter>
"""

print("--- INICIANDO CONEXIÓN NETCONF (PUERTO 830) ---")
with manager.connect(host=host, port=830, username=user, password=password, hostkey_verify=False) as m:
    response = m.get_config(source='running', filter=filter_xml)
    
    # Formatear el XML para que sea legible en el pantallazo
    xml_formateado = xml.dom.minidom.parseString(response.xml).toprettyxml()
    print(xml_formateado)
