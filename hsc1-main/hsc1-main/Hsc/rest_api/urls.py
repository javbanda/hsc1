from django.urls import path
from . import views 

urlpatterns = [
    path('usuario/', views.lista_usuario, name='lista_usuario'),
    path('api/tipousuarios/', views.lista_tipousuario, name='lista_tipousuario'),
    path('api/usuarios/', views.lista_usuario, name='lista_usuario'),
    path('api/comunas/', views.lista_comuna, name='lista_comuna'),
    path('api/regiones/', views.lista_region, name='lista_region'),
    path('api/direcciones/', views.lista_direccion, name='lista_direccion'),
    path('api/ventas/', views.lista_venta, name='lista_venta'),
    path('api/categorias/', views.lista_categoria, name='lista_categoria'),
    path('api/tipoprods/', views.lista_tipoprod, name='lista_tipoprod'),
    path('api/marcas/', views.lista_marca, name='lista_marca'),
    path('api/modelos/', views.lista_modelo, name='lista_modelo'),
    path('api/productos/', views.lista_producto, name='lista_producto'),
    path('api/detalles/', views.lista_detalle, name='lista_detalle'),
    path('usuario/<id>', views.vista_usuario, name='vista_usuario')
    path("mercado-libre/", views.productos_mercadolibre, name="productos_mercadolibre"),
]
