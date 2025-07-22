# core/viewsets.py
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class BaseOptimizedViewSet(viewsets.ModelViewSet):
    """
    ViewSet base que alterna entre .full() y .simple() automáticamente
    y permite serializers diferentes para list y detail.
    """
    pagination_class = DefaultPagination
    simple_serializer_class = None
    full_serializer_class = None

    # def get_queryset(self):        
    #     qs = super().get_queryset()
        
    #     if not (hasattr(qs, 'full') and hasattr(qs, 'simple')):
    #         raise NotImplementedError(
    #         f"❌ El modelo {qs.model.__name__} no está usando un OptimizedManager con full() y simple()."
    #     )

    #     if self.action == 'list':
    #         return qs.simple()
    #     elif self.action in ['retrieve', 'update', 'partial_update']:
    #         return qs.full()
    #     return qs

    # def get_serializer_class(self):
    #     # Cambia el serializer según la acción
    #     if self.action == 'list' and self.simple_serializer_class:
    #         return self.simple_serializer_class
    #     if self.action in ['retrieve', 'update', 'partial_update'] and self.full_serializer_class:
    #         return self.full_serializer_class
    #     return super().get_serializer_class()