# from django.contrib import admin
# from django.urls import path,include
# from api import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('author_api',views.AuthorModelViewSet,basename='author'),
# router.register('book_api',views.BookModelViewSet,basename='book'),



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('auth/', include('rest_framework.urls',namespace='rest_framework')),

# ]



from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

router = DefaultRouter()
router.register('author_api',views.AuthorModelViewSet,basename='author'),
router.register('book_api',views.BookModelViewSet,basename='book'),

router = routers.DefaultRouter()
# Register your DRF app's viewsets with the router

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation for your DRF app",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    # path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]