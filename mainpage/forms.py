from django import forms

from mainpage.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'text',)


class UserForm(forms.ModelForm):

    # class Meta:
        # model =
    pass
