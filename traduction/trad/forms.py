from django import forms

class trd(forms.Form):
    style = forms.TextInput(attrs={'class':"form-control", 'placeholder':"Enter todo e.g. Delete junk files", 'aria-label':"Todo", 'aria-describedby':"add-btn"})
    word = forms.CharField(max_length=120,widget=style)