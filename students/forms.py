from django import forms

from students.models import StudentComplain
from .models import StudentProposal


class StudentForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Name')
    age = forms.IntegerField(min_value=18, max_value=25, required=True, label='AGE')
    check = forms.BooleanField(required=False, label='PRESENT')
    category = forms.ChoiceField(choices=(('student', 'student'), ('other', 'other')), required=True,
                                 label='category', )


class NewStudentComplainForm(forms.ModelForm):
    class Meta:
        model = StudentComplain
        fields = ['name', 'body']


class StudentProposalForm(forms.ModelForm):
    class Meta:
        model = StudentProposal
        fields = ['first_name', 'last_name', 'gender', 'email', 'age']
