from rest_framework import routers

from products import views


router = routers.DefaultRouter()

router.register(r'', views.ProductsViewSet, basename="products")

