from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'age')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'age')
        extra_kwargs = {'password': {'write_only': True}, 'age': {'required': False}}


    def validate(self, attrs):
        attrs = super().validate(attrs)
        username = attrs.get('username')
        email = attrs.get('email')
        if username and email:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                raise serializers.ValidationError("Username or email is already taken.")
        return attrs
    
    def create(self, validated_data):
        
        user = User.objects.create_user(validated_data['username'], 
                                        validated_data['email'], 
                                        validated_data['password'])
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.age = validated_data.get('age')
        user.save()
        return user
    
    