from django.shortcuts import render
from .models import LectureModel
from django.contrib import messages
# Create your views here.
def lecture_base(request):
    if request.method == "POST":
        search_word = request.POST['search_word']
        
        if search_word == "":
            messages.error(request, 'その講義は登録されていません。')
            return render(request, 'userlogapp/search.html', context={})
        
        lecture_names = LectureModel.objects.filter(name__contains=search_word)
        if lecture_names:
            return render(request, 'lecture/lecture.html', context={'lecture_names':lecture_names})
        else:
            messages.error(request, 'その講義は登録されていません。')
            return render(request, 'userlogapp/search.html', context={})
    
    search_word = request.GET['search_word']
    lecture_names = LectureModel.objects.filter(name=search_word)
    return render(request, 'lecture/lecture.html', context={'lecture_names':lecture_names})
