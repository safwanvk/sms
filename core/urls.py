from django.urls import path

from core import views, HodViews

urlpatterns = [
    path('demo', views.showDemoPage, name="demo_page"),
    path('', views.showLoginPage, name="login_page"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="do_login"),
    path('admin_home', HodViews.admin_home, name="admin_home")
]