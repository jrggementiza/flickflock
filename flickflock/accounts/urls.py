from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as accounts_views


app_name = "accounts"
urlpatterns = [
    path('', accounts_views.accounts, name="accounts"),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('signup/', accounts_views.signup, name="signup"),
    path('groups/', accounts_views.groups, name="groups"),
    path('groups/create', accounts_views.group_create, name="groupcreate"),
    path('groups/join', accounts_views.group_join, name="groupcreate"),
]
