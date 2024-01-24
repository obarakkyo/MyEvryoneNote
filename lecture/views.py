from django.shortcuts import render
from .models import LectureModel
# Create your views here.
def lecture_base(request):
    if request.method == "POST":
        search_word = request.POST['search_word']
        lecture_names = LectureModel.objects.filter(name=search_word)
        if lecture_names:
            return render(request, 'lecture/lecture.html', context={'lecture_names':lecture_names})
        
    return render(request, 'lecture/lecture.html', context={})
