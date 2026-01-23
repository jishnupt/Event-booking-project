from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer
# Create your views here.

@api_view(['GET'])
def allevents(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)


@api_view(['GET',"POST"])
def AddEvents(request):
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('event added')


@api_view(['GET','PUT','DELETE'])
def DeletEvent(request,sid):
    event = Event.objects.get(id = sid)
    if request.method == 'GET':
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        event.delete()
        return Response('data deleted')
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

