from rest_framework import serializers
from testapp.models import User, Manager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["u_id", "u_name", "u_email", "inactivated_date"]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ["m_id", "u_id", "m_tel"]
