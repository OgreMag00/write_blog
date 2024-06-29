from django.shortcuts import render
from profile_app.models import Text_post
# Create your views here.


def index(request):
    username = request.user.username
    context = {'posts':Text_post.objects.filter(was_published=True).exclude(username=username)}
    print(context)
    return render(request, 'main_app/index.html', context=context)