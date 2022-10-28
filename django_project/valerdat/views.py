from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import prods, coordprods
from .serializers import prodsSerializer, coordsprodsSerializer


class prodsApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = prods.objects.all()
        serializer = prodsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'ref': request.data.get('ref'),
            'zipcode': request.data.get('zipcode'),
            'store': request.data.get('store'),
            'amount': request.data.get('amount')
        }
        serializer = prodsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class coordsprodsApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = coordprods.objects.all()
        serializer = coordsprodsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
