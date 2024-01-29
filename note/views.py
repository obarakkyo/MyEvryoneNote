from django.shortcuts import render
from lecture.models import LectureModel
from upload.models import UploadModel

# Create your views here.
def note_base(request, lecture_name, lecture_number, page_number):
    models = LectureModel.objects.filter(name=lecture_name)
    note_models = UploadModel.objects.filter(lecture_model=models.first(), lecture_choice=lecture_number)
    return render(request, 'note/note.html', 
                  context={'lecture_name':lecture_name,
                           'lecture_number':lecture_number,
                           'page_number' :page_number,
                           'models'      :models,
                           'note_models':note_models[page_number-1:page_number+5]},)

def note_next_page(request, lecture_name, lecture_number, page_number):
    models = LectureModel.objects.filter(name=lecture_name)
    note_models = UploadModel.objects.filter(lecture_model=models.first(), lecture_choice=lecture_number)

    page_number += 6
    if note_models[page_number-1:page_number+5]:
        return note_base(request, lecture_name, lecture_number, page_number)
    else:
        page_number -= 6
        return note_base(request, lecture_name, lecture_number, page_number)




def note_previous_page(request, lecture_name, lecture_number, page_number):
    if page_number == 1:
        return note_base(request, lecture_name, lecture_number, page_number)
    else:
        page_number -= 6
        return note_base(request, lecture_name, lecture_number, page_number)
