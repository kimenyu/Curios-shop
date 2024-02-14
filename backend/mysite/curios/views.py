from django.shortcuts import render
from .serializers import UserSerializer, LoginSerializer, ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import CustomUser, Product, Order
from .pagination import SmallSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import SmallSetPagination
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import filters
from .permissions import IsAdminUserorReadOnly


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            tokens = serializer.save()
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new product.

    HTTP Methods:
    - POST: Create a new product.

    Request Data:
    - JSON object containing product details.

    Response:
    - 201 Created: Product created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]


    def perform_create(self, serializer):
        """
        Perform the creation of a new product instance.

        Parameters:
        - `serializer` (ProductSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProductListView(ListAPIView):
    """
    ListAPIView for retrieving a list of products.

    HTTP Methods:
    - GET: Retrieve a list of products.

    Query Parameters:
    - `name` (optional): Filter products by name.

    Response:
    - 200 OK: Returns a list of products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SmallSetPagination
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    

    def get_queryset(self):
        """
        Custom queryset to filter products by name.

        Returns:
        - Queryset: Filtered queryset based on query parameters.
        """
        queryset = Product.objects.all().order_by("-id")
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ProductDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific product.

    HTTP Methods:
    - GET: Retrieve details of a specific product.

    Response:
    - 200 OK: Returns details of the requested product.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific product.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific product.

    Request Data:
    - JSON object containing updated product details.

    Response:
    - 200 OK: Product updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_update(self, serializer):
        """
        Perform the update of an existing product instance.

        Parameters:
        - `serializer` (ProductSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProductDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific product.

    HTTP Methods:
    - DELETE: Delete a specific product.

    Response:
    - 204 No Content: Product deleted successfully.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing product instance.

        Parameters:
        - `instance` (Product): The existing product instance to delete.

        Returns:
        - None
        """
        instance.delete()
        
class OrderCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new order.

    HTTP Methods:
    - POST: Create a new order.

    Request Data:
    - JSON object containing order details.

    Response:
    - 201 Created: Order created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform the creation of a new order instance.

        Parameters:
        - `serializer` (OrderSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save(user=self.request.user)
        
class OrderListView(ListAPIView):
    """
    ListAPIView for retrieving a list of orders.

    HTTP Methods:
    - GET: Retrieve a list of orders.

    Response:
    - 200 OK: Returns a list of orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = SmallSetPagination
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        """
        Custom queryset to filter orders by user.

        Returns:
        - Queryset: Filtered queryset based on query parameters.
        """
        queryset = Order.objects.filter(user=self.request.user).order_by("-id")
        return queryset

class OrderDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific order.

    HTTP Methods:
    - GET: Retrieve details of a specific order.

    Response:
    - 200 OK: Returns details of the requested order.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrderUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific order.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific order.

    Request Data:
    - JSON object containing updated order details.

    Response:
    - 200 OK: Order updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Perform the update of an existing order instance.

        Parameters:
        - `serializer` (OrderSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class OrderDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific order.

    HTTP Methods:
    - DELETE: Delete a specific order.

    Response:
    - 204 No Content: Order deleted successfully.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing order instance.

        Parameters:
        - `instance` (Order): The existing order instance to delete.

        Returns:
        - None
        """
        instance.delete()