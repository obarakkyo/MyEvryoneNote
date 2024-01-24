from django.shortcuts import render

# Create your views here.
def upload_base(request):
    return render(request, 'upload/upload.html', context={})