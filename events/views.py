from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy
from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"


class EventUpdateView(UpdateView):
    model = Event
    fields = (
        "title",
        "location",
        "date",
        "members",
    )
    template_name = "event_edit.html"


class EventCancleView(DeleteView):
    model = Event
    template_name = "event_cancle.html"
    success_url = reverse_lazy("event_list")


class EventCreateView(CreateView):
    model = Event
    template_name = "event_new.html"
    fields = (
        "title",
        "location",
        "date",
        "host",
        "members",
    )
