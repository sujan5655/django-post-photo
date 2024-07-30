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


def view_profile(request):

    return render(request,'profile_page.html')

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
            return redirect('/view_profile/')


    context = {
        'form':form
    }


    return render(request,'post.html',context)
