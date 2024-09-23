from django.db import models
from authentification.models import User



# Modelo para la Experiencia de Usuario
class ExperienciaUsuario(models.Model):
    id_experiencia_usuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiencias')

    def __str__(self):
        return self.descripcion


# Modelo para Tipo de Gastos
class TipoGastos(models.Model):
    id_tipo_gastos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo para Gastos del Usuario
class Gastos(models.Model):
    id_gastos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_medida = models.CharField(max_length=50)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos')
    tipo_gastos = models.ForeignKey(TipoGastos, on_delete=models.CASCADE, related_name='gastos')

    def __str__(self):
        return f"{self.nombre} - {self.costo}"


# Modelo para Ingresos del Usuario
class TipoIngresos(models.Model):
    id_tipo_ingresos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ingresos(models.Model):
    id_ingresos = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    valor_ingreso = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingresos')
    tipo_ingresos = models.ForeignKey(TipoIngresos, on_delete=models.CASCADE, related_name='ingresos', null=True)  # Clave foránea hacia TipoIngresos
    #tipo_ingresos = models.ForeignKey(TipoIngresos, on_delete=models.CASCADE, related_name='ingresos')  # Clave foránea hacia TipoIngresos sin null=True


    def __str__(self):
        return f"{self.descripcion} - {self.valor_ingreso}"

# Create your models here.
