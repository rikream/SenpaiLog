from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_user,name="login"), #login opens first
    path("signup/", views.signup,name="signup"),
    path("logout/",views.logout_user, name="logout"),
    path("dashboard/", views.dashboard,name="dashboard")
]