from django.shortcuts import render, redirect
from .models import Text_post

# Create your views here.

def index(request):
    data = []
    
    for i in Text_post.objects.all().filter(username=request.user.username):
        if i.was_published:
            data.insert(0, {"id": i.id,'title':i.title, 'content':i.content, 'date':i.was_published_recently(), 'username':i.username})
        
    context = {'data': data}
    return render(request, 'profile_app/index.html', context=context)


def new_post(request):
    if request.method == 'POST':
        data = request.POST
        username = request.user.username
        content = data.get('content')
        title = data.get('title')
        if data.get('now')=='on':
            was_publish = True
            Text_post().create_post(title=title, content=content, username=username, was_published=was_publish)
            return redirect('/profile')
        else:
            was_publish = False
            Text_post().create_post(title=title, content=content, username=username, was_published=was_publish)
            return redirect('/profile')
    else:
        return render(request, 'profile_app/new_post.html')
    
def draft_list(request):

    
    if request.method == 'POST':
        
        data_r = request.POST
        if len(data_r.getlist('post_id')):
            for i in list(data_r.getlist('post_id')):
                print(i)
                post = Text_post.objects.get(username=request.user.username, id=i)
                post.was_published = True
                post.save(update_fields=["was_published"])
        else:
            data = []
            for i in Text_post.objects.all().filter(username=request.user.username, was_published=False):
                data.insert(0, {'title':i.title, 'content':i.content, 'date':i.was_published_recently(), 'username':i.username, "id":i.id})
            
            context = {'data': data, 'error':'Выберите посты для публикации'}
            return render(request, 'profile_app/draft_list.html', context)
            
            
        
        data = []
        for i in Text_post.objects.all().filter(username=request.user.username, was_published=False):
            data.insert(0, {'title':i.title, 'content':i.content, 'date':i.was_published_recently(), 'username':i.username, "id":i.id})
            
        context = {'data': data}
        return render(request, 'profile_app/draft_list.html', context=context)
    else:
        data = []
        for i in Text_post.objects.all().filter(username=request.user.username, was_published=False):
            data.insert(0, {'title':i.title, 'content':i.content, 'date':i.was_published_recently(), 'username':i.username, "id":i.id})
            
        context = {'data': data}
        return render(request, 'profile_app/draft_list.html', context=context)