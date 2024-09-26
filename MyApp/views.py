from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})


@api_view(["GET", "POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Employees_view(request):

    if request.method == "GET":
        obj = Employee.objects.all()
        serializer = EmployeeSerializer(obj, many=True)
        return Response({"obj": serializer.data})
    if request.method == "POST":
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee added successfully"})
        return Response({"message": "invalid data"})


# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(["POST"])
# def login_api(request):
#     data = request.data
#     serializer = LoginSerializer(data=data)
#     if serializer.is_valid():
#         username = serializer.data["username"]
#         password = serializer.data["password"]

#         employee = authenticate(username=username, password=password)
#         print("*****************")
#     print(employee)

#     if employee is None:
#         return Response({"message": "invalid data"})

#     refresh = RefreshToken.for_user(employee)

#     return Response(
#         {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }
#     )

# return Response({"message": "something went wrong"})
