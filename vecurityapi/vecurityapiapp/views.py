from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from vecurityapiapp.models import (
    CarOwner,
    Car,
    Guard
)
from vecurityapiapp.serializers import (
    CarOwnerSerializer,
    CarSerializer,
    AddCarSerializer,
    GuardSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
import pickle


# When using functions/methods as views
@api_view(['GET', 'POST'])
def car_owner_list(request, format=None):
    """
    List all car owners, or create a new car owner.
    """
    if request.method == 'GET':
        snippets = CarOwner.objects.all()
        serializer = CarOwnerSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarOwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def car_owner_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        car_owner = CarOwner.objects.get(pk=pk)
    except CarOwner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarOwnerSerializer(car_owner)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarOwnerSerializer(car_owner, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car_owner.delete()
        return HttpResponse(status=204)


# Using classes as views
class CarOwnerList(APIView):
    """
    List all car owners, or create a new car owner.
    """

    def get(self, request, format=None):
        carowners = CarOwner.objects.all()
        serializer = CarOwnerSerializer(carowners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'signup successful',
                'error': 0,
                'success': 1,
                'id': serializer.data['id']
            }
            response = pickle.dumps(res)
            jsonresp = pickle.loads(response)
            return Response(jsonresp, status=status.HTTP_201_CREATED)
        else:
            res = {
                'msg': 'signup unsuccessful',
                'error': 1,
                'success': 0,
                'id': 0
            }
            response = pickle.dumps(res)
            jsonresp = pickle.loads(response)
            return Response(jsonresp, status=status.HTTP_400_BAD_REQUEST)


class CarOwnerDetail(APIView):
    """
    Retrieve, update or delete a car owner instance.
    """

    def get_object(self, pk):
        try:
            return CarOwner.objects.get(pk=pk)
        except CarOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        carowner = self.get_object(pk)
        serializer = CarOwnerSerializer(carowner)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        carowner = self.get_object(pk)
        serializer = CarOwnerSerializer(carowner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        carowner = self.get_object(pk)
        carowner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarList(APIView):
    """
    List all cars, or create a new car.
    """

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    """
    Retrieve, update or delete a car owner instance.
    """

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddCar(APIView):
    def post(self, request, format=None):
        car_owner_id = request.data['owner_id']
        license_number = request.data['license_number']
        color = request.data['color']
        pdict = {
            'car_owner_id': car_owner_id,
            'license_number': license_number,
            'color': color
        }

        serializer = AddCarSerializer(data=pdict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnerCars(APIView):
    def get(self, request, oid, format=None):
        cars = Car.objects.filter(car_owner_id=oid)
        serializer = CarSerializer(cars, many=True)
        print(cars)
        return Response(serializer.data)


class CarOwnerLogin(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        if email and password:
            user = CarOwner.objects.filter(email=email).filter(password=password)
            if user.exists():
                res = {
                    'msg': 'Login successful',
                    'error': 0,
                    'success': 1,
                    'id': user[0].id
                }
                response = pickle.dumps(res)
                jsonresp = pickle.loads(response)
                return Response(jsonresp, status=status.HTTP_200_OK)
            else:
                res = {
                    'msg': 'Login unsuccessful',
                    'error': 1,
                    'success': 0,
                    'id': 0
                }
                response = pickle.dumps(res)
                jsonresp = pickle.loads(response)
                return Response(jsonresp, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = {
                'msg': 'No credentials found',
                'error': 2,
                'success': 0,
                'id': 0
            }
            response = pickle.dumps(res)
            jsonresp = pickle.loads(response)
            return Response(jsonresp, status=status.HTTP_400_BAD_REQUEST)


class GuardLogin(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        if email and password:
            user = Guard.objects.filter(email=email).filter(password=password)
            if user.exists():
                res = {
                    'msg': 'Login successful',
                    'error': 0,
                    'success': 1,
                    'id': user[0].id
                }
                response = pickle.dumps(res)
                jsonresp = pickle.loads(response)
                return Response(jsonresp, status=status.HTTP_200_OK)
            else:
                res = {
                    'msg': 'Login unsuccessful',
                    'error': 1,
                    'success': 0,
                    'id': 0
                }
                response = pickle.dumps(res)
                jsonresp = pickle.loads(response)
                return Response(jsonresp, status=status.HTTP_400_BAD_REQUEST)
        else:
            res = {
                'msg': 'No credentials found',
                'error': 2,
                'success': 0,
                'id': 0
            }
            response = pickle.dumps(res)
            jsonresp = pickle.loads(response)
            return Response(jsonresp, status=status.HTTP_400_BAD_REQUEST)
