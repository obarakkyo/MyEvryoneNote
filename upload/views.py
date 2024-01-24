from django.shortcuts import render
from .forms import UploadForm

# Create your views here.
def upload_base(request, lecture_name):
    print(lecture_name)
    forms = UploadForm()
    return render(request, 'upload/upload.html', context={'forms':forms})