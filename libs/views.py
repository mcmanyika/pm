from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import DeployedTickets
from .serializers import *
from .models import t_url, t_dict
from .forms import ContactForm

# Create your views here.


def index(request):
    urls = t_url.objects.all()
    dictionary = t_dict.objects.all()

    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/')

    context = {
        "urls": urls,
        "dictionary": dictionary,
        "form": form,
    }

    template = "base.html"

    return render(request, template, context)

@api_view(['GET', 'POST'])
def tickets_list(request):
    if request.method == 'GET':
        data = DeployedTickets.objects.all()

        serializer = TicketSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)