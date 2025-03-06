from django.shortcuts import render
from app2.models import login
from rest_framework.views import APIView
from rest_framework.response import Response
from app2.models import login
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class LoginListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        logins = login.objects.all()
        serializer = LoginSerializer(logins, many=True)
        return Response(serializer.data)

def dashboard(request):
    data=login.objects.all()
    username2 = request.user.username
    total_salary = sum(user.salary for user in data)

    return render(request, 'd.html', {"login": data,"username2": username2,"total_salary": total_salary})