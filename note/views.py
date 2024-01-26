from django.shortcuts import render
from lecture.models import LectureModel

# Create your views here.
def note_base(request, lecture_name):
    print(type(lecture_name), lecture_name)
    models = LectureModel.objects.filter(name=lecture_name)
    return render(request, 'note/note.html', 
                  context={'lecture_name':lecture_name,
                           'models'      :models})