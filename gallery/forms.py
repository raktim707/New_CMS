from django import forms
from django.forms.widgets import Select
from .models import GalleryPost


class ModelGalleryPostForm(forms.ModelForm):
    class Meta:
        model = GalleryPost
        fields = ['name', 'ImageOrVideo', 'CssClass']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Name/Title For The POST"}),
            'ImageOrVideo': forms.FileInput(attrs={'class': 'form-control', }),
            'CssClass': Select(attrs={'class': 'form-group', }),
        }

        def __init__(self, *args, **kwargs):
            name = kwargs.pop('name', None)
            ImageOrVideo = kwargs.pop('ImageOrVideo', None)
            CssClass = kwargs.pop('CssClass', None)
            super(ModelGalleryPostForm, self).__init__(*args, **kwargs)
            self.fields['name'].text = name
            self.fields['ImageOrVideo'].text = ImageOrVideo
            self.fields['CssClass'].text = CssClass
