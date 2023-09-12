from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Leptup Geminh',
        'amount': '10',
        'price': '9000000',
        'description': 'ini laptop katanya untuk kuliah tapi sebenernya buat geminh'
    }

    return render(request, "main.html", context)