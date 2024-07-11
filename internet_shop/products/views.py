from .models import Products
from .serializer import ProductSerializer
from base.BaseViewSet import BaseViewSet
from .ProductsDAO import ProductsDAO

from authentication.dependencies import role_required

from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
from base.responses import SuccessGetResponse, BadGetResponse
from rest_framework.decorators import action


class ProductsViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    model = Products

    # @role_required(1, 2, 3, 4)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # @role_required(1, 2, 3, 4)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # @role_required(1, 2, 3, 4)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # @role_required(1, 2, 3, 4)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # @role_required(1, 2, 3, 4)
    @extend_schema(
        parameters=[OpenApiParameter('product_name', type=OpenApiTypes.STR,
                                     description='Enter the product name to search for', required=True)],
        responses={200: serializer_class(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_category(self, request):
        product_name = request.query_params.get('product_name', None)
        if product_name is not None:
            categories = ProductsDAO.find_by_name(product_name)
            if not categories:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(categories, many=True)
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])



