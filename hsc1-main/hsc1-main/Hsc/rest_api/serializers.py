from rest_framework import serializers
from inicio.models import TipoUsuario, Usuario

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoUsuario
        fields = ['idTipoUsuario', 'nombreTipo']

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields = ['username','contrasennia','nombre','apellido','email','tipousuario']


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['idComuna', 'nombreCom']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['idRegion', 'nombreReg', 'comuna']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['idDireccion', 'descripcionDir', 'usuario','region']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['idVenta', 'fechaVenta', 'usuario']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nombreCat']

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = ['idTiporod ', 'nombreTipoProd']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['idMarca', 'nombreMarca']

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['idModelo', 'nombreModelo', 'marca']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto','precioProducto','especificacionProd','stockProd', 'imagenProd', 'tipoprod','marca']

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['idDetalle','cantidad','subTotal','venta','producto']

