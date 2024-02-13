from django.shortcuts import render
from .models import BoardModel
from lecture.models import LectureModel
from .forms import BoardFormModel
from django.contrib.auth.models import User

# Create your views here.
def mnvoice_base(request, lecture_name):
    print('lecture_name=', lecture_name, type(lecture_name))

    #formを取得する
    forms = BoardFormModel()

    if request.method == 'POST':
        print('POSTリクエストを受け取りました！')

        forms = BoardFormModel(request.POST or None)
        print('formsにPOST内容を格納')
        if forms.is_valid():
            if request.user.is_authenticated:
                forms.instance.user = request.user
            else:
                print('ログインしていないユーザーです。')
            forms.instance.lecture = LectureModel.objects.get(name=lecture_name)
            forms.save()

    lecture_model = LectureModel.objects.get(name=lecture_name) 

    models = BoardModel.objects.filter(lecture=lecture_model)
    
    return render(request, 'mnvoice/mnvoice.html', 
                  context={'lecture_name':lecture_name, 
                           'models':models,
                           'forms':forms})