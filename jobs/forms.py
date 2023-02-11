from django import forms

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


    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        initial='https://', required=False
    )
    employment_type = forms.ChoiceField(choices=EMPLOYMENT)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.'
    )
    available_days = forms.MultipleChoiceField(
        choices=DAYS, help_text='Select all days that you can work.'
    )
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )