from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from core.telegram import send_greetings


def front(request):
    context = {}
    return render(request, "index.html", context)


@api_view(["GET", "POST"])
def chat(request):
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def send_question_to_chat(request):
    data = request.data
    send_greetings()
    return Response(status=status.HTTP_201_CREATED)