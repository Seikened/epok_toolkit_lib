# Changelog

## [1.12.0] - 2025-08-12
### Added
- Nuevo archivo `epok_toolkit/django/models.py` con mixins para modelos Django: `UUID4Mixin`, `TimeStampMixin`, `SoftDeleteMixin`, `CreatorsMixin`.
- Nueva clase `BaseOptimizedViewSet` y paginación personalizada en `epok_toolkit/django/viewsets.py`.

### Changed
- Actualización de la versión en `pyproject.toml` a `1.12.0`.
- Actualización de la versión en `tag.sh` a `v1.12.0`.
- Corrección en los imports de `epok_toolkit/django/__init__.py` para incluir todos los módulos.
- Corrección en el tipo de campo de `CreatorsMixin` (`UUIDField` a `ForeignKey`) en `models.py`.
- Permisos por defecto ahora requieren autenticación en `BaseOptimizedViewSet`.

### Fixed
- Mejoras menores en la estructura de los archivos y consistencia de imports.

---

Consulta el historial de git para más detalles sobre los cambios realizados.
