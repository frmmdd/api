from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from api_tienda.serializers import LoginSerializer
from api_tienda.serializers import UserSerializer, GroupSerializer, RegisterSerializer
from api_tienda.serializers import StoreSerializer, BrandSerializer, DealSerializer
from api_tienda.models import Store, Brand, Deal
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.http import JsonResponse
from oauth2_provider.views import TokenView

class RegisterEndpoint(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse(serializer.errors, status=400)

class LoginView(TokenView):
    # server_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Login failed!!!'}, status=400)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    # permission_classes = [permissions.IsAuthenticated]
