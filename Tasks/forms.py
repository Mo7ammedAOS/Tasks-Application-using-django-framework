from django import forms


# Add Task input..
class TaskForm(forms.Form):
    text = forms.CharField(max_length=50, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Delete junk files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))