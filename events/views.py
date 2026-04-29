from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventCreationForm


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventCreationForm
    template_name = "event_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.host == self.request.user

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class EventCancleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "event_cancle.html"
    success_url = reverse_lazy("event_list")

    def test_func(self):
        obj = self.get_object()
        return obj.host == self.request.user


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "event_new.html"
    form_class = EventCreationForm

    def form_valid(self, form):
        form.instance.host = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
