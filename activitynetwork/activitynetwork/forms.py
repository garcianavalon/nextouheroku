from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ['act_holder']
        widgets = {
            'datetime': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False})
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})
