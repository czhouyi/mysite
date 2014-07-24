from django.contrib.auth.models import User
from django.core.context_processors import csrf

from models import *
from qq import QQOperator

import time, json

class ContextService:
    def getContext(self, request):
        ctx = {}
        ctx.update(csrf(request))
        token = request.session.get('access_token')
        openid = request.session.get('openid')
        username = request.session.get('username')
        head_image = request.session.get('head_image')
        token_timestamp = request.session.get('token_timestamp')
        
        if self.check(request):
            ctx.update(dict(username=username,head_image=head_image))
        return ctx

    def clearSession(self, request):
        token = request.session.get('access_token')
        openid = request.session.get('openid')
        username = request.session.get('username')
        head_image = request.session.get('head_image')
        token_timestamp = request.session.get('token_timestamp')
        
        if token: del request.session['access_token']
        if openid: del request.session['openid']
        if username: del request.session['username']
        if head_image: del request.session['head_image']
        if token_timestamp: del request.session['token_timestamp']


    def check(self, request):
        token = request.session.get('access_token')
        openid = request.session.get('openid')
        username = request.session.get('username')
        head_image = request.session.get('head_image')
        token_timestamp = request.session.get('token_timestamp')
        
        if openid and token_timestamp and token and username:
            if (long(token_timestamp)-long(time.time())<10*3600*24l):
                return True
        return False


class UserService:

    def create_user(self, username):
        if not User.objects.filter(username=username):
            User(username=username).save()
        return User.objects.get(username=username)

class OpenIdService:

    def create_openid(self, user, openid):
        if not OpenId.objects.filter(openid=openid):
            OpenId(user=user, openid=openid).save()

class TopicService:

    def root(self):
        return Topic.objects.all()[0]

    def topic_tree(self):
        root = {"name":Topic.objects.all()[0]}
        return json.dumps(self.genTree(root))

    def genTree(self, root):
        topic = root["name"]
        children = topic.get_children()
        cld = []
        for child in children:
            cld.append(self.genTree({"name":child}))
        if cld:
            root["children"] = cld
        root["name"] = topic.name
        return root
