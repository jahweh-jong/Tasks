from django import forms

from .models import Task

INPUT_CLASSESS = 'form-control'
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSESS
            })
        }