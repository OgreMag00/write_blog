from django.shortcuts import render, redirect
from profile_app.models import Text_post
# Create your views here.
def index(request, post_id):
    if Text_post.objects.filter(id=post_id).exists():
        post = Text_post.objects.get(id=post_id)
        context = {"title":post.title, "content":post.content, "date":post.was_published_recently()}
        return render(request, 'post_app/index.html', context=context)
    
    else:
        return render(request, 'post_app/index.html', {"error":'Данного поста не существует'})
    
def change(request, post_id):
    username = request.user.username
    
    if username and Text_post.objects.filter(id=post_id, username=username).exists():
        if request.method == 'POST':
            data = request.POST

        
            Text_post.objects.get(id=post_id).change(data.get('new_title'), data.get('new_content'))
            return redirect('profile_index')
        else:
            post = Text_post.objects.get(id=post_id)
            context = {"title":post.title, "content":post.content}
            return render(request, 'post_app/change_post.html', context=context)

    else:
        return redirect('index_page')

def delete(request, post_id):
    username = request.user.username
    
    if username and Text_post.objects.filter(id=post_id, username=username).exists():
        Text_post.objects.filter(id=post_id, username=username).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('index_page')
    
def add_to_draft_list(request, post_id):
    username = request.user.username
    
    if username and Text_post.objects.filter(id=post_id, username=username).exists():
        Text_post.objects.get(id=post_id).to_draft()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('index_page')
    
