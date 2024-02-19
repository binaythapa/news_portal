from django.forms import ModelForm, Textarea
from .models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
