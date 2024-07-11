from rest_framework import routers

from categories import views

router = routers.DefaultRouter()

router.register(r'', views.CategoriesViewSet, basename="category")