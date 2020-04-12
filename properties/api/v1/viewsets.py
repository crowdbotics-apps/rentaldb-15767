from rest_framework import authentication
from properties.models import Address, Unit
from .serializers import AddressSerializer, UnitSerializer
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Address.objects.all()


class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Unit.objects.all()
