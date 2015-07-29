from django import forms

from blogs.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (u'title', u'text',)
        widgets = {
            u'title': forms.TextInput(attrs={u'class': u'form-control'}),
            u'text': forms.Textarea(attrs={u'cols': 50, u'class': u'form-control'}),
        }

    def __init__(self, blog, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.blog = blog

    def save(self, commit=True):
        self.instance.blog = self.blog
        return super(PostCreateForm, self).save(commit)
