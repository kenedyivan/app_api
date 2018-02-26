from rest_framework import serializers
from vecurityapiapp.models import (
    CarOwner,
    Car,
    Guard
)


class CarOwnerSerializer(serializers.ModelSerializer):
    # cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CarOwner
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'country',
                  'address',
                  'password',
                  'created_at',
                  'car_set')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id',
                  'car_owner_id',
                  'license_number',
                  'color',
                  'created_at',)


class AddCarSerializer(serializers.Serializer):
    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        pass

    car_owner_id = serializers.IntegerField()
    license_number = serializers.CharField(required=True, max_length=100)
    color = serializers.CharField(required=True, max_length=10)


class GuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guard
        fields = ('id',
                  'first_name',
                  'last_name',
                  'phone',
                  'email',
                  'account_number',
                  'account_name'
                  )
