from django import forms

class RegisterForm(forms.Form):
    fname = forms.CharField(label='First Name',
        widget=forms.TextInput(attrs={'class':'validate', 'required':'required'}))
    lname = forms.CharField(label='Last Name',
        widget=forms.TextInput(attrs={'class':'validate'}))
    email = forms.EmailField(label='Email',
        widget=forms.TextInput(attrs={'class':'validate', 'type': 'email'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class':'validate'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',
        widget=forms.TextInput(attrs={'class':'validate', 'type': 'email'}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={'class':'validate'}))
