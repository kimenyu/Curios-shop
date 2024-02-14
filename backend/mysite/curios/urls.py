from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, LoginView, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    
    path('curios/create/', ProductCreateView.as_view(), name='create-product'),
    path('curios/list/', ProductListView.as_view(), name='list-product'),
    path('curios/detail/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('curios/update/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    path('curios/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)