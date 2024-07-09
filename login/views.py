from django.shortcuts import render,HttpResponse
from .forms import SignUp

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>You have successfully registered</h1>')
        else:
            form = SignUp()
        return render(request, 'signup.html', {'form': form})