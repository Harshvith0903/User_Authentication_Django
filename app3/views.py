from django.shortcuts import render,redirect
from django.contrib import auth,messages

# Create your views here.
def login (request):
    if request.method=='POST':
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        
        x = auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request, x)
            request.session['username'] = username  #Stored username in session
            return redirect('dashboard')
        else:
            messages.error(request, 'Login unsuccessful!\nIncorrect user ID or password.')
            return redirect('login')
    return render(request,'login.html')

