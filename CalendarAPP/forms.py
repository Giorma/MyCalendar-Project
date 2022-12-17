from django import forms


class DateForm(forms.Form):
    date = forms.DateField(label='Date')
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)