from rest_framework import serializers
from authentification.models import User
from .models import ExperienciaUsuario, TipoGastos, Gastos, Ingresos, TipoIngresos

# Serializador del modelo User
class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User. Incluye los campos adicionales personalizados 
    como nombre, apellido, dirección y estado.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'nombre', 'apellido', 'correo', 'estado', 'email']

# Serializador del modelo ExperienciaUsuario
class ExperienciaUsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ExperienciaUsuario. Serializa la relación con el Usuario.
    """
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='usuario', write_only=True
    )
    
    class Meta:
        model = ExperienciaUsuario
        fields = ['id_experiencia_usuario', 'descripcion', 'usuario', 'usuario_id']

# Serializador del modelo TipoGastos
class TipoGastosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TipoGastos. Serializa el identificador y el nombre.
    """
    class Meta:
        model = TipoGastos
        fields = ['id_tipo_gastos', 'nombre']

# Serializador del modelo Gastos
class GastosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Gastos. Incluye las relaciones con Usuario y TipoGastos.
    """
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='usuario', write_only=True
    )
    
    tipo_gastos = TipoGastosSerializer(read_only=True)
    tipo_gastos_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoGastos.objects.all(), source='tipo_gastos', write_only=True
    )

    class Meta:
        model = Gastos
        fields = ['id_gastos', 'nombre', 'cantidad', 'costo', 'unidad_medida', 'fecha', 'usuario', 'usuario_id', 'tipo_gastos', 'tipo_gastos_id']

# Serializador del modelo TipoIngresos e Ingresos
class TipoIngresosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo TipoIngresos.
    """
    class Meta:
        model = TipoIngresos
        fields = ['id_tipo_ingresos', 'nombre']

class IngresosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Ingresos. Incluye la relación con Usuario y TipoIngresos.
    """
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='usuario', write_only=True
    )

    tipo_ingresos = TipoIngresosSerializer(read_only=True)  # Para mostrar los detalles de TipoIngresos
    tipo_ingresos_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoIngresos.objects.all(), source='tipo_ingresos', write_only=True
    )  # Para escribir el ID de TipoIngresos

    class Meta:
        model = Ingresos
        fields = [
            'id_ingresos', 'descripcion', 'valor_ingreso', 'fecha', 
            'usuario', 'usuario_id', 'tipo_ingresos', 'tipo_ingresos_id'
        ]

