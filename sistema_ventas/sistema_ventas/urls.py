# En sistema_ventas/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from ventas.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ruta para la vista de inicio

    path('', RedirectView.as_view(url='/productos/', permanent=False)),  # Redirecciona a la lista de productos
    path('productos/', include('ventas.urls')),
]
