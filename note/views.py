from django.shortcuts import render
from lecture.models import LectureModel
from upload.models import UploadModel

# Create your views here.
def note_base(request, lecture_name, lecture_number):
    # print(type(lecture_name), lecture_name)
    models = LectureModel.objects.filter(name=lecture_name)
    # print(models, type(models))
    note_models = UploadModel.objects.filter(lecture_model=models.first(), lecture_choice=lecture_number)
    # print(note_models)
    return render(request, 'note/note.html', 
                  context={'lecture_name':lecture_name,
                           'models'      :models,
                           'note_models':note_models},)