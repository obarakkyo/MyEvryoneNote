from django.shortcuts import render

# Create your views here.
def lecture_base(request):
    return render(request, 'lecture/lecture.html', context={})
