from django.urls import path
from .views import index, callofduty, registro, accion, rpg1, deportes, familiar, horror, godofwar, fallguys, baldursgate, dvm3, perfil, recuperar_contrasena



# cada vez que el usuario ingrese al home (url principal, por eso las comillas vacias)...
#se ejecuta la funcion index

urlpatterns=[
    path('', index, name="index"),
    path('callofduty/', callofduty, name="callofduty"),

    path('registro/', registro, name="registro"),
    # otras rutas

    path('rpg1/', rpg1, name="rpg1"),

    path('accion/', accion, name="accion"),

    path('familiar/', familiar, name="familiar"),

    path('deportes/', deportes, name="deportes"),

    path('horror/', horror, name="horror"),

    path('godofwar/', godofwar, name="godofwar"),

    path('fallguys/', fallguys, name="fallguys"),

    path('baldursgate/', baldursgate, name="baldursgate"),

    path('dvm3/', dvm3, name="dvm3"),  

    path('perfil/', perfil, name="perfil"),

    path('recuperar_contrasena/', perfil, name="recuperar_contrasena"),









]