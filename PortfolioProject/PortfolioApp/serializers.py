from rest_framework import serializers
from .models import PortfolioDetails,User

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioDetails  # Ensure this line is present
        fields = '__all__'  # This includes all fields from the model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Ensure this line is present
        fields = '__all__'  # This includes all fields from the model