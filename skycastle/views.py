from django.shortcuts import redirect, render

def Main(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        return render(request, 'main.html')
