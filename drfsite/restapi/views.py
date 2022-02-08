from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restapi
from .serializers import RestapiSerializers


class RestApiViewSet(viewsets.ModelViewSet):
    queryset = Restapi.objects.all()
    serializer_class = RestapiSerializers


# class RestApiView(APIView):
#     def get(self, request):
#         r = Restapi.objects.all()
#         return Response({'posts': RestapiSerializers(r, many=True).data})
#
#     def post(self, request):
#         serializers = RestapiSerializers(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#
#         return Response({'post': serializers.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error', 'Method PUT not allowed!'})
#
#         try:
#             instance = Restapi.objects.get(pk=pk)
#         except:
#             return Response({'Error': 'Object does not exist'})
#
#         serializers = RestapiSerializers(data=request.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({'post': serializers.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'Error', 'Method DELETE not allowed!'})
#
#         try:
#             instance = Restapi.objects.get(pk=pk)
#         except:
#             return Response({'Error': 'Object does not exist'})
#
#         serializers = instance
#         serializers.delete()
#
#         return Response({'post': 'delete post ' + str(pk)})
