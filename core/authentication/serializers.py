from rest_framework import serializers

from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only = True)

class UserSerializer(serializers.ModelSerializer): 

    password: serializers.CharField(required = True, write_only = True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        
class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only = True)
    phone_numer= serializers.CharField(required = True)
    


    class Meta:
        model = CustomUser
        fields = '__all__'