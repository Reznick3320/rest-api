from rest_framework import serializers

from .models import Restapi


class RestapiSerializers(serializers.Serializer):
    userName = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=50)
    register_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Restapi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userName = validated_data.get('userName', instance.userName)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
