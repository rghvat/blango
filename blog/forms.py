from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from blog.models import Comment, Tag, Post
class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('content',)

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()