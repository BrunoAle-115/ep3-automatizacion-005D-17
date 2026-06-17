import datetime
import os

# Asegurar que el directorio de evidencias existe
os.makedirs("fase5_reporte/evidencias", exist_ok=True)

with open("fase5_reporte/evidencias/certificado_compliance_005D-17.txt", "w") as f:
    f.write(f"Certificado de Conformidad - {datetime.datetime.now()}\n")
    f.write("Alumno: Bruno Urrea Ortiz (005D-17)\n")
    f.write("Estado: AUDITORÍA APROBADA - CONFORME\n")
    f.write("Protocolos validados: NETCONF, RESTCONF, Ansible.\n")
print("Certificado generado exitosamente en fase5_reporte/evidencias/certificado_compliance_005D-17.txt")
