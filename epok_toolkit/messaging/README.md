# EPOK Toolkit - Messaging

Este módulo permite el envío de mensajes y archivos por WhatsApp, con manejo de conexión y errores.

## Componentes principales

- **whatsapp.py**: Cliente principal para WhatsApp.
- **whatsapp_instanced.py**: Instancias y utilidades avanzadas para WhatsApp.

## Ejemplo de uso
```python
from epok_toolkit.messaging.whatsapp import WhatsappClient

client = WhatsappClient(token="tu_token", instance_id="tu_instance")
client.send_message(phone="521234567890", text="Hola desde EPOK Toolkit!")
client.send_file(phone="521234567890", file_path="/ruta/archivo.pdf")
```

## Más información
Consulta la documentación de cada archivo para detalles avanzados y ejemplos específicos.
