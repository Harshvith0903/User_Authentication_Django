from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        x = User.objects.create_user(username=username,password=password)
        x.save()
        return redirect('/')
    else:
        return render(request,'b.html')