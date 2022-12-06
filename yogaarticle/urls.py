from django.contrib import admin
from django.urls import include, path
from yogaarticle import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),

    path("article/",views.art,name="art"),
    path("article/<slug:slug>",views.k,name="k"),
    path('postComment', views.postComment, name="postComment"),
    path('register', views.register, name="handleregister"),
    path('log', views.log, name="handlelog"),
    path('signup', views.handleSign, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    # path('/', include('blog.urls'))
]