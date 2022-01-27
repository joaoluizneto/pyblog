from django import forms
from post.models import Post

from django.forms import ClearableFileInput

class NewPostForm(forms.ModelForm):
	posttitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-large'}), required=True)
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
	posttext = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'rows':'20'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Post
		fields = ('posttitle', 'content', 'posttext', 'tags')