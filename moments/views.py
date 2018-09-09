from django.shortcuts import render_to_response
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render_to_response('homepage.html')

def display_user(request):
    user={'name':'coco',
          "region":"zhongshan",
          "motoo":"django is beautiful!",
          "pic":"messi.jpg"
          }
    return render_to_response('user.html',{"user":user})

def display_friends(request):
    return render_to_response('friends.html')

def display_status(request):
    return render_to_response('status.html')

def submit_status(request):
    return render_to_response('my_post.html')
