from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status

from .serializers import RegisterSerializer, FoundSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Register, Found
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# about img_extraction
import base64
import pytesseract
from PIL import Image
import io

from django.contrib.auth.models import User
from rest_framework.views import APIView

class User_data(APIView):
    def get(self, request, pk):
        user_data = get_object_or_404(Register, pk=pk)
        data = RegisterSerializer(user_data).data
        return Response(data)


class FoundItems(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        items = Found.objects.all()[:20]
        data = FoundSerializer(items, many=True).data
        return Response(data)

class CreatItem(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request,format=None):
        author = request.data.get('author')
        img = request.data.get('image')
        # try:
        #     # image = request.FILES['image']
        #     # image = base64.b64encode(image)
        #     # image = base64.b64decode(image)
        #     # image = Image.open(io.BytesIO(image_bytes))
        #     im = Image.open(img)
        #
        # except (KeyError, IOError):
        #    pass
        #
        # #extract img with pytesseract
        # description = pytesseract.image_to_string(img, config=r" --psm 6, --oem 3")

        # print(description)
        data = {'author': author, 'image':img}
        # data = {'author': author, 'image':img, 'description': description}
        serializer = FoundSerializer(data=data)

        if serializer.is_valid():
            found = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            print('LOGIN SUCESS')
            return Response({"token": user.auth_token.key, 'status': status.HTTP_200_OK})
        else:
            return Response({"error": "wrong credential", 'status': status.HTTP_400_BAD_REQUEST})


