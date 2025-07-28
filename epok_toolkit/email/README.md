
# EPOK Toolkit - Email

Este módulo permite el envío de correos electrónicos usando plantillas HTML y texto plano, con configuración visual, registro dinámico y soporte para envío asíncrono.

## Componentes principales

- **engine.py**: Motor para enviar correos electrónicos, soporta adjuntos y plantillas.
- **templates.py**: Registro, renderizado y envoltura visual de plantillas. Permite crear plantillas personalizadas y centralizar la configuración visual.
- **email_async.py**: Envío de correos de forma asíncrona usando Celery, con manejo de reintentos y errores SMTP.

---

## Ejemplos y recomendaciones de uso

### 1. Registro y uso de plantillas
Registra tus propias plantillas y envía correos personalizados.
```python
from epok_toolkit.email.engine import EmailEngine
from epok_toolkit.email.templates import registry

registry.register_template(
    key="welcome",
    subject="🎉 Bienvenido a {company}",
    html_body="<p>Hola {name}, bienvenido a {company}</p>",
    required_vars=["name", "company"]
)

engine = EmailEngine()
engine.send(
    template_key="welcome",
    context={"name": "Fer", "company": "EPOK"},
    recipient="usuario@correo.com"
)
```
**Tip:** El contexto debe incluir todas las variables requeridas por la plantilla.

### 2. Adjuntar archivos (PDF, imágenes, etc.)
```python
engine.send(
    template_key="welcome",
    context={"name": "Fer", "company": "EPOK"},
    recipient="usuario@correo.com",
    attachments={"ticket.pdf": pdf_bytes}
)
```
**Tip:** Los adjuntos se envían como un diccionario `{nombre: bytes}`.

### 3. Envío asíncrono con Celery
Envía correos en segundo plano, ideal para procesos largos o masivos.
```python
from epok_toolkit.email.email_async import send_email


    template_key="welcome",
    context={"name": "Fer", "company": "EPOK"},
    recipient="usuario@correo.com"
)
```
**Tip:** Configura Celery y un broker (Redis, RabbitMQ) para habilitar el envío asíncrono.

### 4. Configuración visual y de empresa
Personaliza el diseño y los datos de tu empresa en `default_settings.py`:
```python
TEMPLATES_SETTINGS = {
    "company": {
        "name": "Company Name",
        "email": "info@compania.com",
        "eslogan": "Eslogan sin definir",
        "footer": "¡Nos vemos pronto!<br><em> El equipo de Company Name 🥳</em>"
    },
    "colors": {
        "background": "#f9fafb",
        "primary": "#4f46e5",
        "text": "#374151",
        "white": "#ffffff"
    }
}
```
**Tip:** El envoltorio visual se aplica automáticamente a los correos HTML.

### 5. Plantillas incluidas por defecto
- password_reset
- welcome
- password_reset_success
- test_app_running

Puedes consultarlas y usarlas directamente:
```python
from epok_toolkit.email.templates import registry
print(registry.templates.keys())
```

---