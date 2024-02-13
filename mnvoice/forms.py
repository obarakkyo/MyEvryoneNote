from django import forms

from .models import BoardModel

class BoardFormModel(forms.ModelForm):

    class Meta:
        model = BoardModel
        fields = ["text"]
        widgets = {
            'text' :forms.Textarea(attrs={'placeholder' : 'コメント',
                                          'name' : 'chat_document',
                                          'id' : 'chat-main'})
        }