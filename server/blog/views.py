from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Blog, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html',{'success':'Account created successfully'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            auth.login(request, user)
            print("user login")
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def create(request):
    form = Blog.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        category = request.POST['category']
        images = request.FILES['images']
        form_info = Blog(title=title, details=details, category=category ,images=images)
        form_info.created_by = request.user
        form_info.save()
        return redirect('home')
    else:
        print('Not Sent')
    return render(request, 'create.html', {'form':form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')


def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        new_title = request.POST['title', '']
        new_content = request.POST['content', '']
        new_image = request.FILES.get('image', blog.image)

        if not new_title:
            return render(request, 'edit.html', {"note": blog, "error": "Title is required."})

        if not new_content:
            return render(request, 'edit.html', {"note": blog, "error": "Content is required."})

        if not new_image:
            return render(request, 'edit.html', {"note": blog, "error": "Image is required."})
        blog.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'blog': blog})


def details(request, model_name, pk):
    model = None
    if model_name == "blog":
        model = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=model)
    context = {"model":model,
               "comments":comments}
    return render(request, 'details.html', context)

@login_required
def comment(request):
    if request.method == 'POST':
        blog_id = request.POST['blog_id']
        content = request.POST['content']
        blog = Blog.objects.get(id=blog_id)
        comment = Comment(blog=blog, content=content, user=request.user)
        comment.save()
        return redirect('details', model_name=blog.__class__.__name__, pk=blog.id)
    return redirect('home')


