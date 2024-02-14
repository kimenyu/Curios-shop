from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, LoginView, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, MerchantRegisterView
# urls.py
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Curios shop",
      default_version='v1',
      description="This is curios shop",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # Add your API URLs here
]



urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    
    path('accounts/merchants/register/', MerchantRegisterView.as_view(), name='register'),
    path('accounts/merchants/login/', LoginView.as_view(), name='login'),
    
    path('curios/create/', ProductCreateView.as_view(), name='create-product'),
    path('curios/list/', ProductListView.as_view(), name='list-product'),
    path('curios/detail/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('curios/update/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    path('curios/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)