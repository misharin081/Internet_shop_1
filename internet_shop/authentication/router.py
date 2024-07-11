from rest_framework import routers

from authentication import views
from .views import UsersViewSet

router = routers.DefaultRouter()

# router.register(r'users', UsersViewSet, basename="register")

