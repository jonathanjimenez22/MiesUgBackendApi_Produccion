from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from bonos.serializers import BonoSerializer
from entrepreneur.models import Bond
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from datetime import datetime
from datetime import timedelta
from dateutil import parser

class Crudbonos(APIView):
    @api_view(['GET', 'POST'])
    def list_bono_view(request ):

        if request.method == 'GET':
            get_data=request.query_params
            bonos = Bond.objects.all()
            if get_data:
                if'entrepreneur' in get_data:
                    bonos=bonos.filter(entrepreneur=get_data['entrepreneur'])
            serializer = BonoSerializer(bonos, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            get_data=request.data
            today = get_data['fecha_inicio']
            todayDay = datetime.strptime(today, "%Y-%m-%d").date()
            days = int(get_data['meses_plazo']) * 30
            later = todayDay + timedelta(days=days)
            request.data['fecha_fin']=later
            serializer = BonoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def user_detail_view(request, pk=None):
        if request.method == 'GET':
            bonos = Bond.objects.get(id=pk)
            serializer = BonoSerializer(bonos)
            return Response(serializer.data)
        elif request.method == 'PUT':
            bonos = Bond.objects.get(id=pk)
            serializer = BonoSerializer(bonos, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            serializer = Bond.objects.get(id=pk)
            serializer.delete()
            return Response({"Mensaje": "bonos  eliminado"}, status=status.HTTP_204_NO_CONTENT)
'''
class bonosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bond.objects.all()
    serializer_class = BonoSerializer

    # Sistema de filtros
    filter_backends = [DjangoFilterBackend,  # edited
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['entrepreneur']
    ordering_fields = ['entrepreneur']'''