from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as accounts_views


app_name = "accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', accounts_views.signup, name="signup"),
    path('groups/', accounts_views.groups, name="groups"),
    path('groups/create', accounts_views.groups_create, name="groupcreate"),
    path('groups/join', accounts_views.groups_join, name="groupjoin"),
    path('groups/invite', accounts_views.groups_invite, name="groupinvite"),
    path('groups/join/<invite_link>', accounts_views.groups_join_via_email, name="groupjoinviaemail"),
]
