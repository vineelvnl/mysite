from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {
        'content': ['if you would like to contact me, email me or message me at', 'EmailID:garsavineel99@gmail.com',
                    'Mobile Number:3136032736','Alternate Email ID:Vinayvny30@gmail.com']})
