from django import forms
from .models import Article,Comment,voite_user

# Form for creating or updating an Article (currently not in use).
class ArticleForm(forms.Form):
    pass
 

# Form for creating or updating comments.
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['title', 'message']
        
        
# Form for submitting a user's vote on an article.
class VoiteForm(forms.ModelForm):
    class Meta:
        model = voite_user
        fields = ['voite',]
        