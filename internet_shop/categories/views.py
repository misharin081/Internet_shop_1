from .models import Categories
from .serializer import CategoriesSerializer
from base.BaseViewSet import BaseViewSet
from base.responses import SuccessGetResponse, BadGetResponse
from .CategotyDAO import CategoryDAO

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter

from authentication.dependencies import role_required



class CategoriesViewSet(BaseViewSet):
    serializer_class = CategoriesSerializer
    model = Categories

    # @role_required(1, 3)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # @role_required(1, 3)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # @role_required(1, 3)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # @role_required(1, 3)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


    # @role_required(1, 2, 3, 4)
    @extend_schema(
        parameters=[OpenApiParameter('category_name', type=OpenApiTypes.STR,
                                     description='Enter the category name to search for', required=True)],
        responses={200: serializer_class(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_category(self, request):
        category_name = request.query_params.get('category_name', None)
        if category_name is not None:
            categories = CategoryDAO.find_by_name(category_name)
            if not categories:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(categories, many=True)
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])
