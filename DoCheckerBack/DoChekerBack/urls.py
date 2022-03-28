from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from sprint0 import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='DoChecker API')

routerClients = routers.DefaultRouter()
routerClients.register('getAll', views.GetAllClientsView,
                basename='getAllClients')

routerTypes = routers.DefaultRouter()
routerTypes.register('getAll', views.GetAllypesView,
                basename='getAllTypes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(routerClients.urls)),
    path('types/', include(routerTypes.urls)),
    path('',schema_view)
]
