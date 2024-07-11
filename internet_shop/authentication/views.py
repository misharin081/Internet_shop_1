from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from base.responses import SuccessPutResponse, BadPutResponse, SuccessGetResponse, BadGetResponse



from .serializer import UserSerializer, LoginSerializer, UsersSerializer, UsersPasswordUpdateSerializer
from database import session_maker
from .models import Users
from base.BaseViewSet import BaseViewSet
from authentication.dependencies import role_required
from .UsersDAO import UsersDAO



import jwt
import datetime
import hashlib


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "msg": "регистрация прошла успешно"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        if request.COOKIES.get('access_key'):
            return Response(data={'message': 'Вы уже авторизованы'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            session = session_maker()
            user = session.query(Users).filter_by(email=email).first()
            session.close()

            payload = {
                "id": user.id,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, 'secret', algorithm="HS256")
            response = Response({"message": "Вход выполнен успешно", "toke": token}, status=status.HTTP_200_OK)
            response.set_cookie(key='access_key', value=token, httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        if request.COOKIES.get('access_key'):
            response.delete_cookie('access_key')
            response.data = {'message': 'Выход выполнен успешно'}
            return response
        response.status_code = status.HTTP_401_UNAUTHORIZED
        response.data = {'message': 'Вы не авторизованы'}
        return response

class UserPasswordUpdateView(APIView):
    serializer_class = UsersPasswordUpdateSerializer

    # @role_required(7)
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        result = UsersDAO.find_by_id(Users, pk)
        if result is None:
            return BadPutResponse(data=[])
        hashed_password = hashlib.md5(request.data['password'].encode()).hexdigest()
        result = UsersDAO.update(Users, pk, {'hashed_password': hashed_password})
        serializer = self.serializer_class(result)
        return SuccessPutResponse(data=serializer.data)


class UsersView(APIView):
    serializer_class = UsersSerializer

    # @role_required(7)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk is None:
            users = UsersDAO.find_all(Users)
            serializer = self.serializer_class(users, many=True)
            return SuccessGetResponse(data=serializer.data)
        else:
            result = UsersDAO.find_by_id(Users, pk)
            if result is None:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(result[0])
            return SuccessGetResponse(data=serializer.data)


class UsersViewSet(BaseViewSet):
    serializer_class = UsersSerializer
    model = Users

    # @role_required(7)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # @role_required(7)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # @role_required(7)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # @role_required(7)
    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = UsersDAO.find_by_id(self.model, pk)
        if result is None:
            return BadPutResponse(data=[])
        hashed_password = hashlib.md5(request.data['hashed_password'].encode()).hexdigest()
        result = UsersDAO.update(self.model, pk, {'hashed_password': hashed_password})
        serializer = self.serializer_class(result)
        return SuccessPutResponse(data=serializer.data)



