from django.urls import path

from .views import (
    EventListView,
    EventDetailView,
    EventUpdateView,
    EventCancleView,
    EventCreateView,
)

urlpatterns = [
    path("<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("<int:pk>/delete/", EventCancleView.as_view(), name="event_cancle"),
    path("new/", EventCreateView.as_view(), name="event_new"),
    path("", EventListView.as_view(), name="event_list"),
]
