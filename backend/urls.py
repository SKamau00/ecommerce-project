from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
]
