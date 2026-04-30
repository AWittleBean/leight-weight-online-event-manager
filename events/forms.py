from django import forms
from django.contrib.auth import get_user_model

from .models import Event

User = get_user_model()


class EventCreationForm(forms.ModelForm):
    member_list = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["member_list"].queryset = User.objects.exclude(pk=user.pk)
        self.fields["member_list"].label_from_instance = lambda user: user.username

    class Meta:
        model = Event
        fields = (
            "title",
            "information",
            "location",
            "date",
            "member_list",
        )
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
