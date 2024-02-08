from django.shortcuts import render

# Create your views here.
def mnvoice_base(request, lecture_name):
    print('lecture_name=', lecture_name, type(lecture_name))

    if request.method == 'POST':
        print('POSTリクエストを受け取りました！')
        print(request.POST['chat_document'])
    
    return render(request, 'mnvoice/mnvoice.html', context={'lecture_name':lecture_name})