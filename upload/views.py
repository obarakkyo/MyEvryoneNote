from django.shortcuts import render, redirect
from .forms import UploadForm
from lecture.models import LectureModel

# Create your views here.
def upload_base(request, lecture_name, lecture_number):
    # print(lecture_name)
    # print(lecture_number)
    forms = UploadForm()

    """もしリクエストがPOSTの場合"""
    if request.method == "POST":
        forms = UploadForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            if request.user.is_authenticated:
                forms.instance.create_user = request.user.username
            else:
                print('ログインしいないユーザーです。')
            forms.instance.lecture_choice = lecture_number
            lecture_instance = LectureModel.objects.get(name=lecture_name)
            forms.instance.lecture_model  = lecture_instance
            forms.save()
        return redirect('note_app:note_base', lecture_name, lecture_number, 1)
    
    lecture_number_notchanged = lecture_number
    lecture_number = lecture_number.replace('st', '回目')
    return render(request, 'upload/upload.html', context={'forms':forms, 'lecture_name':lecture_name, 'lecture_number':lecture_number, 'lecture_number_notchanged':lecture_number_notchanged})