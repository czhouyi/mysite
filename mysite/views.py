from django.http import HttpResponse
from django.core.context_processors import csrf

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import json

import urllib
import time
from qq import QQOperator
from services import *
from blog.services import *
from models import Topic

def treedata(request):
    return HttpResponse(TopicService().topic_tree())

def google(request):
    return render_to_response("google1589042d060ab0f5.html",{})

def hello(request):
    return HttpResponse('Hello World')

def steam(request):
    return render_to_response("index.html",{})

def data(request):
    return render_to_response("data.html",{})

def index(request):
    ctx = ContextService().getContext(request)
    ctx.update(dict(index_posts=PostService().index_posts()))
    return render_to_response("index.html", ctx)

def qqlogin(request):
    request.session['prepath']=request.META['HTTP_REFERER']
    if ContextService().check(request):
        return HttpResponseRedirect("/index/")
    else:
        return HttpResponseRedirect(QQOperator().login_url())

def qqauth(request):
    pre=request.META['HTTP_REFERER']
    import urllib

    html = urllib.urlopen(pre).read()
    print html

    code = request.REQUEST.get('code')
    token = QQOperator().get_token(code)
    openid = QQOperator().get_openid(token)
    qqinfo = QQOperator().get_user_info(token, openid)
    
    user = UserService().create_user(openid)
    OpenIdService().create_openid(user, openid)
    
    request.session['username'] = qqinfo.get('nickname')
    request.session['openid'] = openid
    request.session['access_token'] = token
    request.session['head_image'] = qqinfo.get('figureurl_qq_1').replace('\\','')
    request.session['token_timestamp'] = long(time.time())

    prepath = request.session['prepath']
    del request.session['prepath']
    return HttpResponseRedirect(prepath)

def logout(request):
    prepath = request.META['HTTP_REFERER']
    ContextService().clearSession(request)
    return HttpResponseRedirect(prepath)


