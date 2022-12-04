from django import forms
from .models import Article,Comment,voite_user

class ArticleForm(forms.Form):
    pass
 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['title', 'message']
        
        
class VoiteForm(forms.ModelForm):
    class Meta:
        model = voite_user
        fields = ['voite',]
        