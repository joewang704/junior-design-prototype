from django import forms
from django.contrib.auth.models import User
from models import Profile


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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]

    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'validate', 'required': 'required'}))
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'validate'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_patient', 'disease_interests']

    ROLES = (('0', 'Patient'), ('1', 'Resource'))
    is_patient = forms.ChoiceField(label='Role/Profession',
                                   widget=forms.Select, choices=ROLES)
    disease_interests = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=Profile.DISEASE_CHOICES)


class ForumForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'validate', 'required': 'required'}))


class PostForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'validate', 'required': 'required'}))
    text = forms.CharField(label='Text',
                           widget=forms.Textarea(attrs={'class': 'validate materialize-textarea',
                                                        'required': 'required'}))


class CommentForm(forms.Form):
    text = forms.CharField(label='Text',
                           widget=forms.Textarea(attrs={'class': 'validate materialize-textarea',
                                                        'required': 'required',
                                                        'placeholder': 'Add a comment...'}))
