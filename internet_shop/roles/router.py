from rest_framework import routers

from roles import views

router = routers.DefaultRouter()

router.register(r'', views.RolesViewSet, basename="roles")