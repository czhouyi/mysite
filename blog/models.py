from django.db import models
from django.contrib import admin

from mysite.models import Topic

#from tinymce import models as tmodels

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

class Aphorism(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content
    
class AphorismAdmin(admin.ModelAdmin):
    search_fields = ("content",)

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    topic = models.ForeignKey(Topic, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    cover = models.FileField(upload_to='../static/blog/uploads')
    vtime = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created",)
    search_fields = ("title", "body", )
    filter_horizontal = ('tags',)
    list_filter = ("tags", "created", "topic", )
    date_hierarchy = 'created'

    class Media:
        js = ('/static/tinymce/tinymce.min.js',
              '/static/tinymce/textareas.js',)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "%s: %s" % (self.post.title ,self.body[:60])

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "body", "created")
    search_fields = ("post", "author", "body")
    list_filter = ("created",)
    date_hierarchy = 'created'

admin.site.register(Tag, TagAdmin)
admin.site.register(Aphorism, AphorismAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
