from django import forms
from blog.models import *

class CommentForm(forms.ModelForm):

    #def clean(self):
        #raise forms.ValidationError('bodu=y not null')
     #   return super(CommentForm, self).clean()

    class Meta:
        model = Comment
        exclude = ["post"]
