from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from .forms import UserPostForm


def profile(request,userid): 
    user = User.objects.get(id = userid)
    photos = Photos.objects.filter(user = user)
    context = { 
               'photos':photos
               }
    return render(request,'profile.html',context)


def view_profile(request,username):
    try:
      user=User.objects.get(username=username)
    except User.DoesNotExist:
       return HttpResponse('User with provided username does not exist')
    posts=user.posts.all()
    print(posts)
    
    context={
        'user':user,
        'posts':posts
      
    }
    return render(request,'profile_page.html',context)

def post_view(request):


    if not request.user.is_authenticated:
        # if not logged in
        return HttpResponse("Please Login to Post")   
    

    form = UserPostForm()

   
    if request.method == 'POST':
        form = UserPostForm(request.POST,request.FILES)
        if form.is_valid():
            post_obj = form.save(commit=False) # doesn't save in database
            post_obj.user = request.user
            post_obj.save()
            


    context = {
        'form':form
    }


    return render(request,'post.html',context)
def PostofUser(request):
    
    print(request.GET)
    search=request.GET.get('search')
    if search is not None and search!="":
        posts=Post.objects.filter(title__icontains=search)
    else: 
        posts=Post.objects.all()   
    context={
        'posts':posts,
        'search':search
    }
    return render(request,'ViewPost.html',context)
def viewPostDetail(request,id):
    post=Post.objects.get(id=id)
    context={
        'post':post
    }

    return render(request,'viewPostDetail.html',context)