
# EPOK Toolkit

Esta librería contiene utilidades

## ✉️ Módulo de Email

El módulo de email de `epok_toolkit` permite el envío de correos electrónicos utilizando plantillas HTML predefinidas y personalizables. Está diseñado para ser fácilmente escalable y amigable tanto para usuarios técnicos como no técnicos.

### 🚀 Características principales

- **Templates centralizados** con soporte para HTML y texto plano.
- **Diseño envolvente configurable** con colores y datos de la empresa desde `settings`.
- **Registro dinámico de plantillas** usando un registrador interno (`TemplateRegistry`).
- **Sistema de renderizado robusto** que asegura la presencia de variables requeridas.
- **Soporte para plantillas personalizadas desde settings o módulos externos**.

---

### 🛠️ Cómo funciona

1. Las plantillas se registran automáticamente al iniciar con:
```python
from epok_toolkit.email.templates import registry

registry.register_template(
    key="welcome",
    subject="🎉 Bienvenido a {company}",
    html_body="<p>Hola {name}, bienvenido a {company}</p>",
    required_vars=["name", "company"]
)
```

2. Puedes renderizar una plantilla con variables:
```python
template = registry.templates["welcome"]
rendered = template.render({"name": "Fer", "company": "EPOK"})
```

3. Las plantillas están envueltas automáticamente en un diseño visual (wrapper) que puedes configurar desde `TEMPLATES_SETTINGS` en `settings.py`.

---

### 🧰 Configuración (en `default_settings.py`)

```python
TEMPLATES_SETTINGS = {
    "company": {
        "name": "Congrats",
        "email": "info@compania.com",
        "eslogan": "Eslogan sin definir",
        "footer": "¡Nos vemos pronto!<br><em> El equipo de Congrats 🥳</em>"
    },
    "colors": {
        "background": "#f9fafb",
        "primary": "#4f46e5",
        "text": "#374151",
        "white": "#ffffff"
    }
}
```

---

### 📦 Templates por defecto incluidos

- `password_reset`
- `welcome`
- `password_reset_success`
- `test_app_running`

Puedes consultarlos directamente desde:
```python
from epok_toolkit.email.templates import TEMPLATES
print(TEMPLATES.keys())
```

---

### ✍️ Agregar tus propias plantillas

Desde tu archivo de configuración puedes registrar nuevas plantillas así:

```python
from epok_toolkit.email.templates import registry

registry.register_template(
    key="custom_notification",
    subject="¡Notificación especial para {name}!",
    html_body="<p>Hola {name}, tienes una nueva notificación.</p>",
    required_vars=["name"]
)
```



---

Este componente está diseñado para escalar sin complicaciones y ayudarte a mantener una arquitectura limpia y flexible para notificaciones por correo.
