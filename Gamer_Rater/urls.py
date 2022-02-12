from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from GamerRaterAPI.views import register_user, login_user
from rest_framework import routers
from GamerRaterAPI.views import GameView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
