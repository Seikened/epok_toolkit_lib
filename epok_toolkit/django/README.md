
# EPOK Toolkit - Django

Este módulo agrupa utilidades avanzadas para proyectos Django y Django Rest Framework. Incluye herramientas para optimizar APIs, modelos, autenticación y respuestas.

## Componentes principales

- **cache.py**: Decoradores y clases para caché en APIs y vistas. Permite dos niveles de caché: serialización (`cache_get`) y vista completa (`cache_full`). Incluye `CachedViewSet` para aplicar caché fácilmente en DRF.
- **fields.py**: Campos personalizados para modelos y serializers: UUID, JSON, Float, Decimal, Integer, Char, DateTime, con defaults útiles para proyectos robustos.
- **manager.py**: Managers y QuerySets extendidos para optimizar consultas. `OptimizedManager` permite alternar entre consultas simples y completas, con select_related y prefetch_related configurables.
- **response.py**: Helpers para respuestas estándar y personalizadas en APIs. Incluye funciones para respuestas JSON y archivos, con validación de status y payload estructurado.
- **viewsets.py**: ViewSets extendidos para DRF, con paginación configurable y alternancia automática de serializers y querysets según la acción (`list`, `retrieve`, etc.).
- **utils/**: Utilidades extra, como generación de enlaces mágicos para autenticación sin contraseña (`magic_link.py`).

---

## Ejemplos y recomendaciones de uso

### 1. Caché en APIs
Aplica caché a nivel de serialización y vista completa para mejorar el rendimiento de tus endpoints.
```python
from epok_toolkit.django.cache import CachedViewSet, cache_get, cache_full

class MiVista(CachedViewSet):
    queryset = MiModelo.objects.all()
    serializer_class = MiSerializer

    @cache_get(timeout=60)  # caché de serialización (DRF)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_full(timeout=300)  # caché de vista completa (Django)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
```
**Tip:** Usa los decoradores para endpoints con datos estáticos o de consulta frecuente.

### 2. Campos personalizados
Evita repetir defaults y validaciones en tus modelos.
```python
from epok_toolkit.django.fields import UUIDField, JSONField, StandarFloatField, StandarDecimalField

class MiModelo(models.Model):
    id = UUIDField(primary_key=True)
    datos = JSONField(default=dict)
    precio = StandarFloatField()
    monto = StandarDecimalField()
```
**Tip:** Úsalos para estandarizar tu base de datos y facilitar migraciones.

### 3. Manager y QuerySets optimizados
Alterna entre consultas simples y completas según la vista o acción.
```python
from epok_toolkit.django.manager import OptimizedManager

class MiModelo(models.Model):
    objects = OptimizedManager(
        select_fields_full=['relacion1'],
        prefetch_fields_full=['relacion2'],
        select_fields_simple=[],
        prefetch_fields_simple=[]
    )

# En tu ViewSet puedes usar .full() y .simple() según la acción
```
**Tip:** Mejora el rendimiento de tus endpoints con consultas optimizadas.

### 4. Respuestas API y archivos
Responde con JSON estructurado y archivos adjuntos fácilmente.
```python
from epok_toolkit.django.response import response, file_response

def mi_vista(request):
    return response(data={"msg": "Éxito"}, status_code=200)

def descargar_pdf(request):
    pdf_bytes = generar_pdf()
    return file_response(pdf_bytes, filename="reporte.pdf", content_type="application/pdf")
```
**Tip:** Valida el status y el payload para mantener consistencia en tu API.

### 5. ViewSets extendidos y paginación
Alterna serializers y querysets automáticamente según la acción.
```python
from epok_toolkit.django.viewsets import BaseOptimizedViewSet

class MiViewSet(BaseOptimizedViewSet):
    simple_serializer_class = MiSimpleSerializer
    full_serializer_class = MiFullSerializer
    queryset = MiModelo.objects.all()
```
**Tip:** Usa paginación y alternancia de serializers para APIs escalables.

### 6. Magic Link y autenticación avanzada
Genera enlaces mágicos JWT para login sin contraseña.
```python
from epok_toolkit.django.utils.magic_link import generate_login_magic_token, build_login_magic_link

token = generate_login_magic_token(user)
link = build_login_magic_link(token)
print("Enlace de acceso rápido:", link)
```
**Tip:** Útil para flujos de onboarding, recuperación de acceso y autenticación passwordless.

