from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Matthew Hotmaraja Johan Turnip',
        'npm' : '2206081231',
        'kelas': 'PBP C'
    }

    return render(request, "main.html", context)