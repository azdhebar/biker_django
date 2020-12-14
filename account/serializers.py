from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Account
from vehicles.models import Vehicle
from model.models import Models
from brand.models import Brand
from service.models import Service
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('user','address_fl','address_sl',"city","zip","mobile","is_servicer")

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('id','vehicle_number','model_fk','user')


class VehicleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('id','vehicle_number','model_fk','user')





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','email','username')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Models
        fields=('id','model_name','brand')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=('id','brand')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=('id','servicer','user','brand','vehicle_fk','model_fk','solved','accept','remarks','review','cancel_user','cancel_servicer','problem_image','problem','created_at')

