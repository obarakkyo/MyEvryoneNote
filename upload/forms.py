from django import forms

from .models import UploadModel

lecture_choices = [
    ("1st" , "1回目"),
    ("2st" , "2回目"),
    ("3st" , "3回目"),
    ("4st" , "4回目"),
    ("5st" , "5回目"),
    ("6st" , "6回目"),
    ("7st" , "7回目"),
    ("8st" , "8回目"),
    ("9st" , "9回目"),
    ("10st" , "10回目"),
    ("11st" , "11回目"),
    ("12st" , "12回目"),
    ("13st" , "13回目"),
    ("14st" , "14回目"),
]

class CustomFileInput(forms.ClearableFileInput):
    def __init__(self, attrs=None, accept=None):
        super().__init__(attrs)
        if accept:
            self.attrs['accept'] = accept

class CustomImageInput(forms.ClearableFileInput):
    def __init__(self, attrs=None, accept=None):
        super().__init__(attrs)
        if accept:
            self.attrs['accept'] = accept

class UploadForm(forms.ModelForm):
    note_title = forms.CharField(label='ノートタイトル')
    file       = forms.FileField(label='ノートをアップロード', widget=CustomFileInput(accept=".pdf"))
    image_file = forms.ImageField(label='ノート表紙をアップロード', widget=CustomImageInput(accept=".png, .jpg"))
    # lecture_choice = forms.ChoiceField(label='第〇回目講義', choices=lecture_choices)
    # lecture_model  = forms.ModelChoiceField(label='講義名')

    class Meta:
        model = UploadModel
        fields = ["note_title", "file", "image_file"]
    