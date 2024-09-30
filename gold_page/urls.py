from django.urls import path

from .views import home, create_user, login_user, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('create_account/', create_user, name='create_account'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
]