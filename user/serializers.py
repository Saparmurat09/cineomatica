from rest_framework import serializers
from .models import User, ClubCard

from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'email',
            'phone',
            'is_staff',
            'birth_date',
            'password', 
            'password2',
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            birth_date=validated_data['birth_date'],
        )
        user.set_password(validated_data['password'])
        user.username = validated_data['email']
        user.save()

        clubcard = ClubCard.objects.create(user=user)
        clubcard.save()

        return user
