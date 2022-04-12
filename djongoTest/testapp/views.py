from djongo.models import json
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import UserSerializer, ManagerSerializer
from testapp.models import User, Manager


class UserViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)


class ManagerViewSets(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)
