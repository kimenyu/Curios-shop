# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser, Product, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to login with provided credentials.")
        else:
            raise serializers.ValidationError("Must provide email and password.")

        return data

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'quantity']


    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.

    Fields:
    - `id`: The unique identifier for the order.
    - `user`: The associated user (serialized using CustomUserSerializer).
    - `product`: The associated cart (serialized using CartSerializer).
    - `quantity`: The quantity of the order.
    - `created_at`: The date and time when the order was created.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Order
        fields = ['id', 'user',  'created_at', 'product', 'quantity']
        
    def create(self, validated_data):
        """
        Create a new order instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the order.

        Returns:
        - `Order`: The created order instance.
        """

        
        # Now, create the order with the contact info instance
        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing order instance.

        Parameters:
        - `instance` (Order): The existing order instance to update.
        - `validated_data` (dict): Validated data for updating the order.

        Returns:
        - `Order`: The updated order instance.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.product = validated_data.get('status', instance.product)
        instance.save()
        return instance