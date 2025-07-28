# EPOK Toolkit - Email

Este módulo permite el envío de correos electrónicos usando plantillas HTML y texto plano, con configuración visual y registro dinámico de plantillas.

## Componentes principales

- **engine.py**: Funciones para enviar correos electrónicos.
- **templates.py**: Registro y renderizado de plantillas.
- **email_async.py**: Envío de correos de forma asíncrona.

## Ejemplo de uso
```python
from epok_toolkit.email.engine import send_email
from epok_toolkit.email.templates import registry

registry.register_template(
    key="welcome",
    subject="🎉 Bienvenido a {company}",
    html_body="<p>Hola {name}, bienvenido a {company}</p>",
    required_vars=["name", "company"]
)

rendered = registry.templates["welcome"].render({"name": "Fer", "company": "EPOK"})
send_email(
    to=["usuario@correo.com"],
    subject=rendered.subject,
    html_body=rendered.html_body
)
```

## Configuración
Configura los datos de empresa y colores visuales en `default_settings.py`.

## Plantillas incluidas
- password_reset
- welcome
- password_reset_success
- test_app_running

## Más información
Consulta la documentación de cada archivo para detalles avanzados y ejemplos específicos.
