from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    global response
    try:
        movie = Movie.objects.get(slug=slug)
        response = {"success": True}
    except:
        response["error"] = "Bunday ma'lumot yo'q"
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method == "GET":
        serializer = MovieSerializers(movie)
        response["data"] = serializer.data
        return Response(data=response, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = MovieSerializers(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        id = movie.pk
        movie.delete()
        return Response(data={"id": f"{id} o'chirili"})





# @api_view(['POST'])
# def ism_api(request):
#     ism = request.data["ism"]
#     year = request.data["year"]
#     return Response(data={"ism": f"salom {ism}", "year": f"tugilgan yili: {year}"})