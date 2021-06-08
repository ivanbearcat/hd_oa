from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    path = request.path.split('/')[1]
    return render(request,'public/index.html',{'user': request.user.username,
                                               'path1':path,
                                               'page_name1':u'主页'})
