from django.shortcuts import render
from machina.models import Forum
# Create your views here.


def forum_home(request):
        forums = Forum.objects.all()
        return render(request, 'forum_app/forum_home.html', {'forums': forums})