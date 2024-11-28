from rest_framework import serializers
from .models import Individual, Admin
from django.contrib.auth import authenticate

# Serializer for Individual model
class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['individual_id', 'first_name', 'last_name', 'birth_date', 'gender', 'contact_info']

# Serializer for Admin registration and login
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Admin.objects.create_user(**validated_data)
        return user

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
