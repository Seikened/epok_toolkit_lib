# EPOK Toolkit - PDF

Este módulo permite la generación de tickets PDF personalizados usando ReportLab y plantillas gráficas.

## Componentes principales

- **ticket_pdf.py**: Generador de tickets PDF.
- **fuentes/**: Fuentes tipográficas para PDFs.
- **plantillas/**: Imágenes y plantillas gráficas para tickets.

## Ejemplo de uso
```python
from epok_toolkit.pdf.ticket_pdf import TicketPDF

ticket = TicketPDF(
    nombre="Fer León",
    evento="Concierto EPOK",
    fecha="2025-08-01",
    qr_data="https://epok.com/ticket/12345"
)

pdf_bytes = ticket.generate()
with open("ticket.pdf", "wb") as f:
    f.write(pdf_bytes)
```

## Más información
Consulta la documentación de cada archivo para detalles avanzados y ejemplos específicos.
