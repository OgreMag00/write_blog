from django.shortcuts import render, redirect
from .models import Text_post

# Create your views here.

def index(request):
    data = []
    
    for i in Text_post.objects.all().filter(username=request.user.username):
        data.insert(0, {'title':i.title, 'content':i.content, 'date':i.was_published_recently(), 'username':i.username})
        
    context = {'data': data}
    return render(request, 'profile_app/index.html', context=context)


def new_post(request):
    if request.method == 'POST':
        data = request.POST
        username = request.user.username
        content = data.get('content')
        title = data.get('title')
        Text_post().create_post(title=title, content=content, username=username)
        return redirect('/profile')
    else:
        return render(request, 'profile_app/new_post.html')