from django.urls import path, include
from .views import iniciar,iniciar_sesion, inicio, inicioadmin, registrar_m, registrarse, newProd,addprod,vistamod,eliminarProducto,menuadmin,micadmin,tecladoadmin,mouseAdmin,ramAdmin,graficaAdmin,procesadorAdmin,mostrarTeclado,teclado,mostrarMic,micro,mostrarMouse,mouse,mostrarGrafica,grafica,mostrarRam,ram,mostrarProcesador,procesador,carrito,perfilusuario,edicionProducto,editarProducto, mostrarperfil, modificarPerfil ,agregar_producto,eliminar_producto,restar_producto,limpiar_producto, valor_dolar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Pagina iniciar/ Solo carga pagina
    path('iniciar/', iniciar, name="iniciar"),

    # Valida usuario / Aqui tenemos las consultas
    path('iniciarsesion/', iniciar_sesion, name="iniciarsesion"),

    # Página principal
    path('', inicio, name="inicio"),

    path('indexadmin', inicioadmin, name="indexadmin"),

    path('registrar/', registrar_m, name="registrar"),
    path('registrarse/', registrarse, name="registrarse"),

    # Agregar producto
    path('agregar2/', newProd, name="addProd"),
    path('agregar/', addprod, name="agregarprod"),

    # Modificar producto
    path('modificar/', vistamod, name="modificar"),
    path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),

    # Menú admin
    path('menuadmin/', menuadmin, name="menu_admin"),

    # Vistas admin por categoría
    path('micadmin/<id>', micadmin, name="micadmin"),
    path('tecladoadmin/<id>', tecladoadmin, name="tecladoadmin"),
    path('mouseAdmin/<id>', mouseAdmin, name="mouseAdmin"),
    path('ramAdmin/<id>', ramAdmin, name="ramAdmin"),
    path('graficaAdmin/<id>', graficaAdmin, name="graficaAdmin"),
    path('procesadorAdmin/<id>', procesadorAdmin, name="procesadorAdmin"),

    # Mostrar productos por tipo
    path('teclados/<id>', mostrarTeclado, name="teclados"),
    path('teclados/<idk>/<usuario>', teclado, name="teclado"),

    path('microfonos/<id>', mostrarMic, name="mostrarMic"),
    path('microfono/<idmic>/<usuario>', micro, name="micro"),

    path('mouses/<id>', mostrarMouse, name="mostrarMouse"),
    path('mouses/<idm>/<usuario>', mouse, name="mouse"),

    path('graficas/<id>', mostrarGrafica, name="mostrarGrafica"),
    path('graficas/<idg>/<usuario>', grafica, name="grafica"),

    path('rams/<id>', mostrarRam, name="mostrarRam"),
    path('rams/<idr>/<usuario>', ram, name="ram"),

    path('procesadores/<id>', mostrarProcesador, name="mostrarProcesador"),
    path('procesadores/<idp>/<usuario>', procesador, name="procesador"),

    # Carrito
    path('carrito/<id>', carrito, name="carrito"),
    path('agregar3/<int:idProducto>/<str:usuario>', agregar_producto, name="Add"),
    path('eliminar/<int:idProducto>/<str:usuario>', eliminar_producto, name="Del"),
    path('restar/<int:idProducto>/<str:usuario>', restar_producto, name="Sub"),
    path('limpiar/<str:usuario>', limpiar_producto, name="CLS"),

    # Usuario
    path('miperfil/<id>', perfilusuario, name="miperfil"),
    path('mostrarperfil/<id>', mostrarperfil, name="mostrarperfil"),
    path('modificarPerfil/<id>', modificarPerfil, name="modificarPerfil"),

    # Edición de productos
    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),

    # API interna
    path('api/', include('rest_api.urls')),

    # 🌐 API externa: valor del dólar
    path('dolar/', valor_dolar, name="valor_dolar"),
]

# Archivos multimedia (en desarrollo)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
