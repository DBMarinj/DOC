from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import User, ExperienciaUsuario, TipoGastos, Gastos, Ingresos, TipoIngresos
from .serializers import (
     UserSerializer, ExperienciaUsuarioSerializer, 
    TipoGastosSerializer, GastosSerializer, IngresosSerializer, TipoIngresosSerializer
)


# ViewSet para el modelo Usuario
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet para el modelo ExperienciaUsuario
class ExperienciaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ExperienciaUsuario.objects.all()
    serializer_class = ExperienciaUsuarioSerializer


# ViewSet para el modelo TipoGastos
class TipoGastosViewSet(viewsets.ModelViewSet):
    queryset = TipoGastos.objects.all()
    serializer_class = TipoGastosSerializer


# ViewSet para el modelo Gastos
class GastosViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los gastos del usuario autenticado.
    """
    serializer_class = GastosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Sobrescribe el método para filtrar los gastos del usuario autenticado.
        """
        user = self.request.user  # Usuario autenticado
        return Gastos.objects.filter(usuario_id=user.id)  # Filtra los gastos por usuario_id

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado al crear un gasto.
        """
        serializer.save(usuario=self.request.user)


# ViewSet para el modelo Ingresos
class IngresosViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los ingresos del usuario autenticado.
    """
    serializer_class = IngresosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Sobrescribe el método para filtrar los ingresos del usuario autenticado.
        Aquí nos aseguramos de obtener todos los ingresos históricos del usuario autenticado
        """
        user = self.request.user  # Usuario autenticado
        return Ingresos.objects.filter(usuario_id=user.id)  # Filtra por usuario.id (ID del usuario autenticado)

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado al crear un ingreso.
        """
        serializer.save(usuario=self.request.user)


class TipoIngresosViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los tipos de ingresos.
    """
    queryset = TipoIngresos.objects.all()  # Obtiene todos los tipos de ingresos
    serializer_class = TipoIngresosSerializer
    permission_classes = [permissions.IsAuthenticated]
