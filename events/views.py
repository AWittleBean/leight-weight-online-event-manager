from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


def event_list(request):
    events = Event.objects.all()
    return render(request, "home.html", {"events": events})
