from django import forms

from .models import Event


class EventCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["member_list"].label_from_instance = lambda user: user.username

    class Meta:
        model = Event
        fields = (
            "title",
            # "information",
            "location",
            "date",
            "member_list",
        )
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
