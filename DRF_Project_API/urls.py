from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('author_api',views.AuthorModelViewSet,basename='author'),
router.register('book_api',views.BookModelViewSet,basename='book'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),

]




# from django.contrib import admin
# from django.urls import path
# from api import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('studentapi/', views.StudentList.as_view()),
#     path('api/', views.Author_List_Create.as_view()),
#     # path('studentapi/', views.StudentCreate.as_view()),
#     # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
#     # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
#     # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
#     # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
#     # path('studentapi/<int:pk>/', views.StudentRetrive_Destroy.as_view()),
#     # path('api/<int:pk>/', views.StudentRetrive_Destroy_Update.as_view()),
# ]