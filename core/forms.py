from django import forms
from .models import Post
#Model Form
class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description','image')


