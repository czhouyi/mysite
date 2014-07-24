from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect as redirect
from mysite.views import *
from blog.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^google1589042d060ab0f5.html$', google),
    url(r'^index/$', index),
    url(r'^$', lambda x: redirect('/index/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^blog/$', postlist),
    url(r'^blog/post/$', lambda x: redirect('/blog/')),
    url(r'^blog/tag/$', lambda x: redirect('/blog/')),
    url(r'^blog/post/(\d+)/$', post),
    url(r'^blog/tag/(\d+)/$', postlistbytag),
    url(r'^add_comment/$', add_comment),
    url(r'^add_comment/(\d+)/$', add_comment),
    url(r'^steam/$', steam),
    url(r'^qqlogin/$', qqlogin),
    url(r'^qqauth/$', qqauth),
    url(r'^logout/$', logout),
    url(r'^treedata/$', treedata),
    url(r'^data/$', data),
)
