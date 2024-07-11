from .models import Client
from .serializer import ClientSerializer
from base.BaseViewSet import BaseViewSet

from authentication.dependencies import role_required

class ClientsViewSet(BaseViewSet):
    serializer_class = ClientSerializer
    model = Client

    # @role_required(1, 2, 3, 4)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # @role_required(1, 2, 3, 4)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



