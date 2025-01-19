from django.urls import path
from . import views

urlpatterns = [
    path("register_user/",views.register_user,name="register_user"),
    path("update_profile/",views.update_profile,name="update_profile"),
    path("create_blog/",views.create_blog,name="create_blog"),
    path("blog_list/",views.blog_list,name="blog_list"),
    path("blogs/<slug:slug>", views.get_blog, name="get_blog"),
    path("blog_update/<int:pk>/",views.blog_update,name="blog_update"),
    path("blog_delete/<int:pk>/",views.blog_delete,name="blog_delete"),
    path("get_username", views.get_username, name="get_username"),
    path("get_userinfo/<str:username>", views.get_userinfo, name="get_userinfo"),
]
