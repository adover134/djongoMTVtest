from djongo.models import json
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import UserSerializer, ManagerSerializer
from testapp.models import User, Manager
from testapp.decorator import request_converting_to_object_id


class UserViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @request_converting_to_object_id
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    @request_converting_to_object_id
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    @request_converting_to_object_id
    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    @request_converting_to_object_id
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)


class ManagerViewSets(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    @request_converting_to_object_id
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    @request_converting_to_object_id
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    @request_converting_to_object_id
    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    @request_converting_to_object_id
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)
