from .models import Roles
from .serializer import RolesSerializer
from base.BaseViewSet import BaseViewSet
from database import session_maker
from authentication.dependencies import role_required
from .RolesDAO import RolesDAO


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
from base.responses import SuccessGetResponse, BadGetResponse


class RolesViewSet(BaseViewSet):
    serializer_class = RolesSerializer
    model = Roles

    # @role_required(7)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def pertial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # @role_required(7)
    @extend_schema(
        parameters=[OpenApiParameter('role_name', type=OpenApiTypes.STR,
                                     description='Enter the role name to search for', required=True)],
        responses={200: RolesSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_role(self, request):
        role_name = request.query_params.get('role_name', None)
        if role_name is not None:
            roles = RolesDAO.find_by_name(role_name)
            if not roles:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(roles, many=True)
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])
