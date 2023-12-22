
from django.urls import path
from .views import ListUsers ,CustomAuthToken,RegisterApi,user_delete


urlpatterns = [
    path('api/users/',ListUsers.as_view()),
    path('api/token_auth/', CustomAuthToken.as_view()),
    path('api/register/',RegisterApi.as_view()),
    path('api/logout/',user_delete.as_view())
]