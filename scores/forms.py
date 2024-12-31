from django import forms
from .models import Student, Score

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['subject', 'score']
