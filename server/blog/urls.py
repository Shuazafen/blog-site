from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('detail/<str:model_name>/<int:pk>', views.details, name='detail'),
    path('comment', views.comment, name='comment'),
    path('create/', views.create, name='create'),
    path('blog/update/<int:pk>', views.blog_update, name='blog_update'),
    path('blog/delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('logout/', views.logout, name="logout"),
   # path('comment/delete/<int:pk>', views.delete_comment, name='delete_comment'),
    #path('comment/update/<int:pk>', views.update_comment, name='update_comment')
   # path('comment/update/<int:pk>', views.upate_comment, name='update_comment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)