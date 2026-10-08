from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post , Comment , Like , Follow , Profile
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already exists"})

        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        Profile.objects.create(user=user)

        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request,"login.html",{"error": "Invalid username or password"})
    return render(request, "login.html")

@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")

    liked_posts = Like.objects.filter(
        user=request.user
    ).values_list("post_id", flat=True)

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "liked_posts": liked_posts
        }
    )

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    profile_user = request.user

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    user_posts = Post.objects.filter(
        user=profile_user
    ).order_by("-created_at")

    return render(
        request,
        "profile.html",
        {
            "profile_user": profile_user,
            "followers_count": followers_count,
            "following_count": following_count,
            "user_posts": user_posts
        }
    )
  
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST["content"]

        Post.objects.create(user=request.user,content=content)

        return redirect("home")

    return render(request, "create_post.html")

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        content = request.POST["content"]

        post = Post.objects.get(id=post_id)

        Comment.objects.create(post=post,user=request.user,content=content)

    return redirect("home")

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(post=post,user=request.user)

    if not created:
        like.delete()

    return redirect("home")

@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)

    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(follower=request.user,following=user_to_follow)
        if not created:
            follow.delete()

    return redirect("home")

@login_required
def users_view(request):
    users = User.objects.exclude(id=request.user.id)

    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list("following_id", flat=True)

    return render(
        request,
        "users.html",
        {
            "users": users,
            "following_ids": following_ids
        }
    )

@login_required
def update_profile_image(request):

    if request.method == "POST":

        profile, created = Profile.objects.get_or_create(
            user=request.user
        )

        if "profile_image" in request.FILES:

            profile.profile_image = request.FILES["profile_image"]

            profile.save()

    return redirect("profile")