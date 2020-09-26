from django.db import models

# Create your models here.
class Proveedor(models.Model):
	ruc = models.CharField(max_length=11)
	razon_social = models.CharField(max_length=20)
	telefono = models.CharField(max_length=9)

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)

class Localizacion(models.Model):
	distrito = models.CharField(max_length=20)
	provincia = models.CharField(max_length=20)
	departamento = models.CharField(max_length=20)

class Producto(models.Model):
	# Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)

	#Métodos
    def precio_final(self):
	    self.precio * (1 - self.descuento)

    def sku(self):
	    codigo_categoria = self.categoria.codigo.zfill(4)
	    codigo_producto = str(self.id).zfill(6)

	    return f'{codigo_categoria}-{codigo_producto}'

class Pedido(models.Model):
	#Atributos
	fechaCreacion = models.DateField(auto_now=True)
	estado = models.CharField(max_length=20)
	fechaEntrega = models.DateField()
	direccionEntrega = models.CharField(max_length=200)
	tarifa = models.FloatField()

	#Relaciones
	pass

class DetallePedido(models.Model):
	#Atributos
	cantidad = models.IntegerField()
	subtotal = models.FloatField()

	#Relaciones

class Usuario(models.Model):
	#Atributos
	email = models.EmailField()
	password = models.CharField(max_length=50)
	documentoIdentidad = models.CharField(max_length=8)
	nombres = models.CharField(max_length=100)
	apellidoPaterno = models.CharField(max_length=100)
	apellidoMaterno = models.CharField(max_length=100)
	genero = models.CharField(max_length=25)
	fechaNacimiento = models.DateField()
	fechaCreacion = models.DateField(auto_now=True)
	estado = models.CharField(max_length=50)

	#Relaciones
	pass

class Cliente(Usuario):
	#Atributos
	preferencias = models.CharField(max_length=150)
	tipoUsuario = models.CharField(max_length=150, default="cliente")

	#Relaciones

class Colaborador(Usuario):
	#Atributos
	#Relaciones
	pass