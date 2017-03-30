from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    fname = forms.CharField(label='First Name',
                            widget=forms.TextInput(attrs={'class': 'validate', 'required': 'required'}))
    lname = forms.CharField(label='Last Name',
                            widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'validate', 'type': 'email'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'validate'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'validate', 'type': 'email'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'validate'}))


class ProfileForm(forms.ModelForm):
    # jgluck: not sure the best place to put this?
    ROLES = (('1', 'Patient'), ('2', 'Resource'))
    class Meta:
        model=User
        fields=['first_name', 'last_name']

    first_name = forms.CharField(label='First Name',
                            widget=forms.TextInput(attrs={'class': 'validate', 'required': 'required'}))
    last_name = forms.CharField(label='Last Name',
                            widget=forms.TextInput(attrs={'class': 'validate'}))

    # role = forms.ChoiceField(label='Role/Profession',
    #                          widget=forms.Select, choices=ROLES)

class ForumForm(forms.Form):
    title = forms.CharField(label='Title',
                        widget=forms.TextInput(attrs={'class':'validate', 'required': 'required'}))

class PostForm(forms.Form):
    title = forms.CharField(label='Title',
                        widget=forms.TextInput(attrs={'class':'validate', 'required': 'required'}))
    text = forms.CharField(label='Text',
                        widget=forms.Textarea(attrs={'class':'validate materialize-textarea',
                                                     'required': 'required'}))

class CommentForm(forms.Form):
    text = forms.CharField(label='Text',
            widget=forms.Textarea(attrs={'class':'validate materialize-textarea',
                                         'required': 'required',
                                         'placeholder': 'Add a comment...'}))

