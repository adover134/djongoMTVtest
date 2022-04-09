from rest_framework import serializers
from testapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["_id", "u_name", "u_email"]