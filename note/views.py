from django.shortcuts import render

# Create your views here.
def note_base(request):
    return render(request, 'note/note.html', context={})