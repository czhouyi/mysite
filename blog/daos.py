from blog.models import *

class TagDao:

    def all(self):
        return Tag.objects.all()

class AphorismDao:
    def today(self):
        from datetime import date
        ym = int(date.today().strftime("%Y%m"))
        d = date.today().day
        cnt = Aphorism.objects.count()
        lstr = str(ym**d)[::-1]
        idx = (long(lstr)) % cnt
        return Aphorism.objects.all()[idx].content

class PostDao:

    def all(self):
        return Post.objects.all()
    
    def all_short(self, tagid=None):
        posts = None
        if tagid:
            posts = Post.objects.filter(tags__id=tagid).order_by("-created")
        else:
            posts = Post.objects.all().order_by("-created")
        for post in posts:
            post.body = "%s......" % post.body[:150]
        return posts

    def get(self, pk):
        return Post.objects.get(pk=pk)

    def increaseVTime(self, pk):
        post = self.get(pk)
        post.vtime = post.vtime + 1
        post.save()

class CommentDao:

    def all(self, post=None):
        if post:
            return Comment.objects.filter(post=post).order_by("created")
        else:
            return Comment.objects.all().order_by("created")
