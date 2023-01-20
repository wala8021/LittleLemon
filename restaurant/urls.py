from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('api-token-auth/', obtain_auth_token),
    
    #all the djoser endpoints work automatically without explicitly defining them here.. examples below... find more on https://djoser.readthedocs.io/en/latest/getting_started.html
    # /auth/users/ POST new user registration
    # /auth/users/ GET request to list all users
    # /auth/token/login/ POST to get token
]
