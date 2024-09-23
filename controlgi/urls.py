from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    UserViewSet, ExperienciaUsuarioViewSet,
    TipoGastosViewSet, GastosViewSet, IngresosViewSet, TipoIngresosViewSet
)

# Creamos el router y registramos los ViewSets
router = DefaultRouter()
#router.register(r'usuarios', UserViewSet)
router.register(r'experiencias', ExperienciaUsuarioViewSet)
router.register(r'tipo-gastos', TipoGastosViewSet)
router.register(r'gastos', GastosViewSet,basename='gastos')
router.register(r'ingresos', IngresosViewSet,basename='ingresos')
router.register(r'tipo-ingresos', TipoIngresosViewSet, basename='tipo-ingresos')

# Definimos las URLs de la aplicación
urlpatterns = [
    
    path('apli/', include(router.urls)),  # Incluye todas las rutas generadas por el router
    
    
]