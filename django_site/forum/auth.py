from django.contrib.auth.models import User

def createuser(email, password, fname, lname):
    user = User.objects.create_user(
        username=email, email=email, password=password)
    user.first_name = fname
    user.last_name = lname
    user.save()
