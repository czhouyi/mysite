from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from blog.models import *
from blog.forms import *
from blog.services import *
from mysite.services import ContextService
# Create your views here.

def postlist(request):
    ctx = ContextService().getContext(request)
    
    posts = PostService().pagedPosts(request)
    cmtcnt = CommentService().cmt_counts()
    tags = TagService().all()

    ctx.update(dict(tags=tags, posts=posts, cmtcnt=cmtcnt))

    return render_to_response("blog.html", ctx)

def postlistbytag(request, tagid):
    ctx = ContextService().getContext(request)
    cmtcnt = CommentService().cmt_counts()
    tags = TagService().all()
    posts = PostService().pagedPosts(request, tagid)
    ctx.update(dict(posts=posts, cmtcnt=cmtcnt, tags=tags, tagid=int(tagid)))

    return render_to_response("blog.html", ctx)


def post(request, pk):
    ctx = ContextService().getContext(request)

    post = PostService().get(pk)
    comments = CommentService().all(post)
    commentForm = CommentForm()
    ctx.update(dict(post=post, comments=comments, form=commentForm))
    ctx.update(csrf(request))
    
    PostService().increaseVTime(pk)
    return render_to_response("post.html", ctx)

def add_comment(request, pk):
    p = request.POST
    if p.has_key("body") and p["body"]:
        author = request.session.get('username')

        comment = Comment(post=PostService().get(pk))
        #cf = CommentForm(p, instance=comment)

        #comment = cf.save(commit=False)
        comment.body = p['body']
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))
