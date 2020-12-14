from django.urls import  path,include

from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.logout_ac,name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),


]