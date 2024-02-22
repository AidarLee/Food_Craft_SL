from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from mobile.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'user-groups', GroupViewSet, basename='user_groups')
# router.register(r'products', ProductsList_APIViewSet, basename='products')
# router.register(r'chemicals', Chemicals_APIView, basename='chemicals')
# router.register(r'fatacids', Fatacids_APIView, basename='fatacids')
# router.register(r'minerals', Minerals_APIView, basename='minerals')

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    
    path('aminoacid/', Aminoacid_APIView.as_view(), name='aminoacid-list'),
    path('products/', ProductsList_APIViewSet.as_view(), name='products-list'),
    path('chemicals/', Chemicals_APIView.as_view(), name='chemicals-list'),
    path('minerals/', Minerals_APIView.as_view(), name='minerals-list'),
    path('fatacids/', Fatacids_APIView.as_view(), name='fatacids'),
    path('process-recipe/', ProcessRecipeAPIView.as_view(), name='process-recipe'),
    path('login-user/', LoginView.as_view(), name='login'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls