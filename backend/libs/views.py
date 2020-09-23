from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import messages
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
