from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.

# Blog Function where Posts will Appear.
def Blog(request):
    posts = Post.objects.all()
    return render(request, 'BlogApp/blog.html', {'posts':posts})

# Dashboard Function will provide operations via authentication like (CRUD).
def dashboard(request):
    posts = Post.objects.all()
    user = request.user
    full_name = user.get_full_name()
    groups = user.groups.all()
    return render(request, 'BlogApp/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':groups})

# This Function contains About Deatail of Project.
def about(request):
    return render(request, 'BlogApp/about.html')

# Here User(Author) will register for login by passing some of the Required Fields.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!, You became an Author.')
            user = form.save()
            group = Group.objects.get(name='Author') #we will assign signup user into Author.
            user.groups.add(group)
    else:
        form = SignUpForm()

    return render(request, 'BlogApp/signup.html' ,{'form':form})

# After Signup, By Unique username and password you will be logged into Blog.
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully !!')
                    return HttpResponseRedirect('Blog')
        else:
            form = LoginForm()
        return render(request, 'BlogApp/log_in.html' ,{'form':form})
    else:
        return HttpResponseRedirect('Blog')


# Logout function will auto redirect to you on Portfolio.
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

# Add Post Function
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title ,desc=desc)
                pst.save()
                messages.success(request,'Post Added SuccessFully!!')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'BlogApp/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/log_in/')

#Update Post Function
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Post Updated SuccessFully!!')
        else:
             pi = Post.objects.get(pk=id)
             form = PostForm(instance=pi)
        return render(request, 'BlogApp/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/log_in/')

# Delete Post Function
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('/log_in/')