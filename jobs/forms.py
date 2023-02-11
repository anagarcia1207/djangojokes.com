from django import forms
from datetime import datetime

class JobApplicationForm(forms.Form):
    EMPLOYMENT = (
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
        ('cw', 'Contract work')
    )


    DAYS = (
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday')
    )

    YEARS = range(1900, datetime.now().year+1)


    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    birth_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=YEARS,
            empty_label=("Choose Year", "Choose Month", "Choose Day")
        )
    )
    email = forms.EmailField()
    website = forms.URLField(
        widget=forms.URLInput(attrs={
            'size': '50',
            'placeholder': 'https://www.example.com'
        })
    )
    employment_type = forms.ChoiceField(choices=EMPLOYMENT)
    start_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years= ['2023', '2024'],
            empty_label=("Choose Year", "Choose Month", "Choose Day")
        )
    )
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text='Check all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min':'10.00', 'max':'100.00', 'step':'.25'}
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )