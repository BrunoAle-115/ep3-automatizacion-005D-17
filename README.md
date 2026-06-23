# Informe Técnico de Implementación - Consultora Digital Norte SA

**Ingeniero de Automatización:** Bruno Urrea Ortiz (005D-17)

## 1. Objetivo del proyecto
Se implementó un ciclo completo de automatización de red para integrar un nuevo router a la infraestructura de Consultora Digital Norte SA. El objetivo final fue asegurar el aprovisionamiento estandarizado, validando de forma programática que el equipo cumpla con las normativas corporativas antes de su paso a producción.

## 2. Alcance
El proyecto abarcó el respaldo del estado inicial, la habilitación de protocolos de gestión y la inyección de la configuración base (hostname, interfaces, banners y sincronización de tiempo). Quedaron fuera del alcance las configuraciones de enrutamiento dinámico, políticas de firewall y calidad de servicio (QoS). El trabajo se limitó a interacciones automatizadas, excluyendo configuraciones manuales por CLI en la fase de despliegue.

## 3. Infraestructura utilizada
* **Estación de control:** DEVASC VM (Ubuntu Linux).
* **Dispositivo de red:** Router Cisco CSR1000v virtualizado.
* **Sistema Operativo del Router:** Cisco IOS-XE.
* **Herramientas de software:** pyATS/Genie, Ansible, Python 3 (librerías `ncclient` y `requests`).

## 4. Tecnologías empleadas y justificación
* **pyATS / Genie:** Se utilizó para capturar el *baseline* inicial y el estado final del equipo, ya que permite documentar el estado operativo conectándose vía SSH estándar sin depender de APIs previamente habilitadas.
* **Ansible:** Se eligió para la fase de aprovisionamiento por su enfoque declarativo, permitiendo aplicar la configuración completa garantizando la idempotencia del proceso.
* **NETCONF:** Se utilizó para la auditoría profunda de la configuración aplicada, ya que permite extraer la jerarquía completa del sistema en formato XML estructurado respaldado por modelos YANG.
* **RESTCONF:** Se implementó como segunda capa de validación para consultar recursos específicos de la API del router mediante peticiones HTTPS, obteniendo respuestas ágiles en formato JSON.

## 5. Configuración aplicada
A continuación, se detallan los parámetros inyectados en el dispositivo corporativo:

| Parámetro | Valor Aplicado |
| :--- | :--- |
| Hostname | RTR-CONDIG |
| IP Loopback Gestión | 10.5.17.1 |
| Máscara Loopback | 255.255.255.0 |
| Descripción WAN | Enlace-WAN-Los-Angeles |
| Servidor NTP | 1.1.1.1 |

## 6. Resultados de validación
La auditoría independiente arrojó los siguientes resultados:

| Criterio Evaluado | Protocolo | Resultado |
| :--- | :--- | :--- |
| Parámetros Base | NETCONF (Puerto 830) | CONFORME |
| Estado Operativo API | RESTCONF (Puerto 443) | CONFORME |

## 7. Conclusiones
El equipo ha sido aprovisionado exitosamente y ha superado todas las auditorías de estado. La infraestructura refleja un estado 100% idempotente y alineado con el modelo de datos de la empresa. El router se declara **CONFORME** y está listo para ser entregado a la unidad de operaciones para su puesta en producción.
