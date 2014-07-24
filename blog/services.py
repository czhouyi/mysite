from django.core.paginator import Paginator, InvalidPage, EmptyPage

from blog.daos import *

class TagService:
    def all(self):
        return TagDao().all()

class PostService:
    def index_posts(self):
        posts = PostDao().all_short()[:3]
        return posts


    def pagedPosts(self, request, tagid=None):
        posts = PostDao().all_short(tagid)
        paginator = Paginator(posts, 10)

        try:
            page = int(request.GET.get("page", "1"))
        except ValueError:
            page = 1

        try:
            posts = paginator.page(page)
        except (InvalidPage, EmptyPage):
            posts = paginator.page(paginator.num_pages)

        return posts

    def get(self, pk):
        return PostDao().get(int(pk))

    def increaseVTime(self, pk):
        return PostDao().increaseVTime(int(pk))

class CommentService:
    def cmt_counts(self):
        '''
        Here returns a dict.
        It contains the count of all posts
        '''
        cmtcnt = {}
        for post in PostDao().all():
            cmtcnt[post.id] = CommentDao().all(post=post).count()
        return cmtcnt
        
    def all(self, post):
        return CommentDao().all(post)
