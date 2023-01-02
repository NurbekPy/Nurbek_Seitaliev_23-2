from django import forms


class CategoryCreateForm(forms.Form):
    title = forms.CharField(min_length=3)
    description = forms.CharField(widget=forms.Textarea())
    author = forms.CharField(min_length=3)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=3, label='Оставьте рекомендации')
