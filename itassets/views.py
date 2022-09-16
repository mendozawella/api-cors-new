from django.http import JsonResponse
from .models import Itasset
from .serializers import ItassetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def itasset_list(request, format=None):

    if request.method == 'GET':
        itasset = Itasset.objects.all()
        serializer = ItassetSerializer(itasset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = ItassetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def itasset_detail(request, id, format=None):

    try:
        itasset = Itasset.objects.get(pk=id)
    except Itasset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItassetSerializer(itasset)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = ItassetSerializer(itasset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
            itasset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
