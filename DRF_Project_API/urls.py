from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register('author_api', views.AuthorModelViewSet, basename='author')
router.register('book_api', views.BookModelViewSet, basename='book')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]





















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