from django.urls import path
from apps.accounts.views import LoginUser, RegisterUser, LogoutUser
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
