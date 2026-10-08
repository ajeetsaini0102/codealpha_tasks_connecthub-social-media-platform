from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/update-image/", views.update_profile_image, name="update_profile_image"),
    path("create-post/", views.create_post, name="create_post"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
    path("users/", views.users_view, name="users"),
]