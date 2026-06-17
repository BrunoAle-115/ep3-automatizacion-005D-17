# Proyecto de Automatización de Redes - Consultora Digital Norte SA
**Alumno:** Bruno Urrea Ortiz (005D-17)  
**Institución:** Duoc UC - Ingeniería en Conectividad y Redes

## Descripción del Proyecto
Implementación de un ciclo de vida de automatización para infraestructura de red utilizando Cisco IOS-XE, Ansible, Genie (pyATS), NETCONF y RESTCONF.

## Diagrama de Flujo del Proceso


## Fases del Proyecto
1. **Fase 1 (Baseline):** Captura de estado inicial mediante Genie y pyATS.
2. **Fase 2 (Aprovisionamiento):** Despliegue de configuración corporativa mediante Ansible con idempotencia total (`changed=0`).
3. **Fase 3 (Validación NETCONF):** Auditoría de parámetros mediante XML sobre el puerto 830.
4. **Fase 4 (Validación RESTCONF):** Auditoría de API mediante JSON sobre el puerto 443.
5. **Fase 5 (Compliance):** Generación de certificado de auditoría final.

## Resultados
* Estado final: **CONFORME**
* Todas las tareas de Ansible cumplen con el principio de idempotencia.
* Protocolos de gestión validados exitosamente.

---
*Proyecto desarrollado para la evaluación EP3 de Automatización.*
