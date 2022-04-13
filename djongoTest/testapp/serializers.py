from rest_framework import serializers
from testapp.models import User, Manager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields 변수에는 CRUD에 사용될 필드 값들을 적는다.
        fields = ["u_name", "u_email", "inactivated_date", "u_access_token"]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ("u_id", "m_tel")
